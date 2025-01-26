# ETL Pipeline Using Astro and Apache Airflow

This repository contains an Extract, Transform, and Load (ETL) pipeline developed using Astro (Astronomer) and Apache Airflow. The pipeline is designed to automate data workflows, ensuring efficient extraction, transformation, and loading of weather data into a PostgreSQL database.

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
##### ├── SQL/ # SQL files for database schema and queries ##### ├── plugins/ 
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

