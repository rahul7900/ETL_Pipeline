from airflow import DAG
from airflow.providers.http.hooks.http import HttpHook
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.decorators import task
from airflow.utils.dates import days_ago
from datetime import datetime
from datetime import date
import requests
import json



# Latitude and longitude of the desired location (London in this case)

LATITUDE = '51.5074'
LONGITUDE = '-0.1278'

POSTGRES_CONN_ID = f"postgres_default"
API_CONN_ID = 'Open_meteo_api'

# Default arguments

default_args = {
    'owner': 'airflow',
    'start_days':days_ago(1)
}

# DAG

with DAG(dag_id='weather_etl_pipeline',
default_args=default_args,
schedule_interval='@daily',
catchup=False,start_date=datetime(2025, 1, 26, 00, 00)) as dag:

    @task()
    def extract_weather_data():
        # Create an instance of the HttpHook class to interact with the Open-Meteo API

        # Use HTTP Hook to get weather data
        http_hook = HttpHook(method='GET', http_conn_id=API_CONN_ID)

        # Build the API endpoint
        # https://api.open-meteo.com/v1/forecast?latitude={LATITUDE}&longitude={LONGITUDE}&current_weather=true
        end_point = f'/v1/forecast?latitude={LATITUDE}&longitude={LONGITUDE}&current_weather=true'

        # Make the request via HTTP Hook
        response = http_hook.run(end_point)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to retrieve weather data. Status code: {response.status_code}")
        
    @task()
    def transform_weather_data(weather_data):
        # Transform the weather data into a format suitable for the Postgres database
        current_weather = weather_data['current_weather']
        transformed_data = {
            'latitude':LATITUDE,
            'longitude':LONGITUDE,
            'temperature':current_weather['temperature'],
            'windspeed':current_weather['windspeed'],
            'winddirection':current_weather['winddirection'],
            # 'humidity':current_weather['humidity'],
            'weathercode':current_weather['weathercode']
        }
        return transformed_data
    
    @task()
    def load_weather_data(transformed_data):
        # Create a connection to the Postgres database
        pg_hook = PostgresHook(postgres_conn_id=POSTGRES_CONN_ID)
        conn = pg_hook.get_conn()
        cursor = conn.cursor()

        # Creating a table if it doesn't exist
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS weather_data (
                    latitude FLOAT, 
                    longitude FLOAT, 
                    temperature FLOAT,
                    windspeed FLOAT,
                    winddirection FLOAT,
                    weathercode FLOAT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    Primary Key (timestamp)
                );
            ''')
        
        # Insert the transformed data into the Postgres database
        cursor.execute('''
        INSERT INTO weather_data (latitude, longitude, temperature, windspeed, winddirection,weathercode,timestamp)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
                       ''', (
                        transformed_data['latitude'],
                        transformed_data['longitude'],
                        transformed_data['temperature'],
                        transformed_data['windspeed'],
                        transformed_data['winddirection'],
                        # transformed_data['humidity'],
                        transformed_data['weathercode'],
                        datetime.now()
                        ))
        
        conn.commit()
        cursor.close()
        conn.close()
    
    # DAG Workflow - ETL Pipeline
    weather_data = extract_weather_data()
    transform_data = transform_weather_data(weather_data)
    load_weather_data(transform_data)

