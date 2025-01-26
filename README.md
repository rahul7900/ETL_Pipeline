# ETL Pipeline Using Astro and Apache Airflow

This repository contains an Extract, Transform, and Load (ETL) pipeline developed using Astro (Astronomer) and Apache Airflow. The pipeline is designed to automate data workflows, ensuring efficient extraction, transformation, and loading of weather data into a PostgreSQL database.

Overview
========

Welcome to Astronomer! This project was generated after you ran 'astro dev init' using the Astronomer CLI. This readme describes the contents of the project, as well as how to run Apache Airflow on your local machine.

Project Contents
================

Your Astro project contains the following files and folders:

- dags: This folder contains the Python files for your Airflow DAGs. By default, this directory includes one example DAG:
    - `example_astronauts`: This DAG shows a simple ETL pipeline example that queries the list of astronauts currently in space from the Open Notify API and prints a statement for each astronaut. The DAG uses the TaskFlow API to define tasks in Python, and dynamic task mapping to dynamically print a statement for each astronaut. For more on how this DAG works, see our [Getting started tutorial](https://www.astronomer.io/docs/learn/get-started-with-airflow).
- Dockerfile: This file contains a versioned Astro Runtime Docker image that provides a differentiated Airflow experience. If you want to execute other commands or overrides at runtime, specify them here.
- include: This folder contains any additional files that you want to include as part of your project. It is empty by default.
- packages.txt: Install OS-level packages needed for your project by adding them to this file. It is empty by default.
- requirements.txt: Install Python packages needed for your project by adding them to this file. It is empty by default.
- plugins: Add custom or community plugins for your project to this file. It is empty by default.
- airflow_settings.yaml: Use this local-only file to specify Airflow Connections, Variables, and Pools instead of entering them in the Airflow UI as you develop DAGs in this project.

Deploy Your Project Locally
===========================

1. Start Airflow on your local machine by running 'astro dev start'.

This command will spin up 4 Docker containers on your machine, each for a different Airflow component:

- Postgres: Airflow's Metadata Database
- Webserver: The Airflow component responsible for rendering the Airflow UI
- Scheduler: The Airflow component responsible for monitoring and triggering tasks
- Triggerer: The Airflow component responsible for triggering deferred tasks

2. Verify that all 4 Docker containers were created by running 'docker ps'.

Note: Running 'astro dev start' will start your project with the Airflow Webserver exposed at port 8080 and Postgres exposed at port 5432. If you already have either of those ports allocated, you can either [stop your existing Docker containers or change the port](https://www.astronomer.io/docs/astro/cli/troubleshoot-locally#ports-are-not-available-for-my-local-airflow-webserver).

3. Access the Airflow UI for your local Airflow project. To do so, go to http://localhost:8080/ and log in with 'admin' for both your Username and Password.

You should also be able to access your Postgres Database at 'localhost:5432/postgres'.

Deploy Your Project to Astronomer
=================================

If you have an Astronomer account, pushing code to a Deployment on Astronomer is simple. For deploying instructions, refer to Astronomer documentation: https://www.astronomer.io/docs/astro/deploy-code/

Contact
=======

The Astronomer CLI is maintained with love by the Astronomer team. To report a bug or suggest a change, reach out to our support.


## Features
- **Dynamic Data Extraction**: Fetches weather data from an external API.
- **Data Transformation**: Processes raw weather data into a clean, structured format.
- **Database Integration**: Stores the processed data in a PostgreSQL database.
- **Error Handling**: Ensures robust error logging and retries.
- **Scheduler**: Uses Apache Airflow for task orchestration and scheduling.

## Project Structure

##### ├── dags/ │
##### ├── etlweather.py # Main Airflow DAG file defining the ETL workflow 
##### ├── include/ │ 
##### ├── SQL/ # SQL files for database schema and queries 
##### ├── plugins/ 
##### │ └── custom_operators/ # Custom Airflow operators (if any) 
##### ├── Dockerfile # Containerization for deployment 
##### ├── requirements.txt # Python dependencies 
##### ├── README.md # Project documentation 
##### └── .astro/ # Astro project configuration


## Prerequisites

Ensure the following tools are installed before starting:
- Docker
- Python 3.8+
- Apache Airflow 2.0+
- Astronomer CLI

## Setup

### 1. Clone the Repository

git clone https://github.com/your_username/your_repo.git
cd your_repo

### 2. Install Dependencies

pip install -r requirements.txt

### 3. Start the Astro Project

Initialize your Astro project using Docker:

astro dev start

### 4. Environment Variables

Create a .env file to securely store your API keys, database credentials, and other environment-specific configurations. Example:

##### API_KEY=your_api_key
##### POSTGRES_HOST=localhost
##### POSTGRES_PORT=5432
##### POSTGRES_USER=your_user
##### POSTGRES_PASSWORD=your_password
##### POSTGRES_DB=weather_data

## How It Works

### ETL Workflow

Extract: Fetch weather data from the API using a Python function.

Transform: Clean and format the data (e.g., converting timestamps, handling missing values).

Load: Insert the transformed data into the PostgreSQL database.

### Airflow DAG

The DAG is defined in dags/etlweather.py and includes the following tasks:

extract_data: Fetch data from the weather API.

transform_data: Process raw data into a structured format.

load_data: Store the data in the database.

### Usage

Running the Pipeline

Start the Astro project:

astro dev start

Open the Airflow UI in your browser:

http://localhost:8080

Trigger the etl_weather DAG to execute the pipeline.

### Testing

Unit tests for individual tasks and functions can be added in the tests/ directory. To run tests, use:

pytest

## Future Improvements

Add automated data validation checks.

Integrate with cloud-based data storage (e.g., AWS S3, Google Cloud Storage).

Schedule DAGs using Cron expressions for specific intervals.

Implement CI/CD pipelines for deployment.

## Contributing

Contributions are welcome! Please follow these steps:

Fork the repository.

Create a feature branch.

Commit your changes.

Submit a pull request.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contact

For questions or collaboration, Rahul Singh.


