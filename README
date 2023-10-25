# Flight Data ETL Pipeline

This repository contains a data pipeline for extracting flight data from an external API, transforming it, and loading it into a PostgreSQL database. The pipeline is managed using Docker containers, and you don't need to install Airflow separately.

## Prerequisites

Make sure you have the following software installed:

- Docker: [Installation Guide](https://docs.docker.com/get-docker/)
- Docker Compose: [Installation Guide](https://docs.docker.com/compose/install/)

## Usage

1. **Build Docker Images:**

   Build the required Docker images for the data pipeline components:

   \\\ash
   docker-compose build
   \\\

2. **Start Docker Containers:**

   Start the Docker containers for the database, Airflow, and Jupyter:

   \\\ash
   docker-compose up -d
   \\\

3. **Access Airflow Web Interface:**

   Open your web browser and access the Airflow web interface at [http://localhost:8080](http://localhost:8080).

   - Username: airflow
   - Password: airflow

4. **Trigger Airflow DAG:**

   Navigate to the "DAGs" page and turn on the "flight_data_etl" DAG. Trigger the DAG to start the data pipeline. You can trigger the DAG manually from the Airflow web interface.

   [Airflow DAG Trigger Link](http://localhost:8080/dags/flight_data_etl/grid?root=)

5. **Explore Data with Jupyter:**

   Access the Jupyter Notebook environment to explore the data. Open your web browser and go to the Jupyter environment at [http://localhost:10000/lab](http://localhost:10000/lab).

   - No password is required, as a token is generated.

## Data Pipeline Details

The data pipeline performs the following tasks:

- Fetches flight data from an external API.
- Transforms the data to prepare it for database insertion.
- Loads the transformed data into a PostgreSQL database.

## Folder Structure

- \dags/\: Contains Airflow DAG definitions (Note: Airflow is included within the Docker containers).
- \sql/\: Stores SQL scripts for database creation and data loading.
- \scripts/\: Python scripts for ETL and data exploration.
- \data/\: Directory for storing CSV data.

## ETL Process

The ETL process is managed by Airflow within the Docker container and involves the following tasks:

1. Extract data from an external API.
2. Transform the data, including data cleaning and structure adjustments.
3. Load the transformed data into the PostgreSQL database.

## Additional Information

For further information on how the pipeline works and data exploration, refer to the Jupyter Notebook located at [http://localhost:10000/lab/tree/call_to_database.ipynb](http://localhost:10000/lab/tree/call_to_database.ipynb).

Feel free to explore and analyze the flight data with Jupyter Notebooks.
