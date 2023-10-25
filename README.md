# Flight Data ETL Pipeline

This repository contains a data pipeline for extracting flight data from an external API, transforming it, and loading it into a PostgreSQL database. The pipeline is managed using Docker containers.

## Prerequisites

Make sure you have the following software installed:

- Docker: [Installation Guide](https://docs.docker.com/get-docker/)
- Docker Compose: [Installation Guide](https://docs.docker.com/compose/install/)

## Architecture

The data pipeline encompasses the entire ETL (Extract, Transform, Load) process for flight data:

1. **External API:** Flight data is initially fetched from an external source through the AviationStack API. This data includes essential flight information.

2. **Data Transformation:** Post-fetch, the pipeline proceeds to transform the data by cleaning it, adjusting column names, and ensuring data consistency.

3. **PostgreSQL Database:** Transformed data is loaded into a PostgreSQL database. This database serves as a central repository for efficient data storage, enabling various analytics and reporting operations.

- **Apache Airflow:** Orchestrates the pipeline and automates the ETL process according to predefined schedules.

- **Jupyter Notebook:** Offers an interactive platform for exploring and analyzing flight data.




## Usage

1. **Build Docker Images:**

   Build the required Docker images for the data pipeline components:

   ```bash
   docker-compose build
   ```

2. **Start Docker Containers:**

   Start the Docker containers for the database, Airflow, and Jupyter:

   ```bash
   docker-compose up -d
   ```

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
   
   [Jupyter Notebook Link](http://localhost:10000/lab/tree/call_to_database.ipynb)


## Airflow Folder Structure

- `/dags`: Contains Airflow DAG definitions (Note: Airflow is included within the Docker containers).
- `/data`: Directory for storing CSV data.

## Postgres Folder Structure

- `Dockerfile`: Custom Dockerfile to include init scripts.
- `.sql`: Init scripts to create tables and databases.

## Future Improvements

1. **Data Quality Checks:**
   - Implement checks to ensure that required data fields are not missing in the extracted data.
   - Verify that date fields are in a valid format (e.g., 'YYYY-MM-DD').
   - Validate that numeric fields, such as flight numbers, contain only integers.

2. **Error Handling:**
   - In case of an API request failure, set up a retry mechanism with a maximum retry count.
   - When a data transformation error occurs, log the error message and proceed with the pipeline without crashing.

3. **Scheduled DAG Runs:**
   - Configure Airflow to run the DAG at regular intervals, such as daily or hourly.
   - Set up dependencies between tasks to ensure that the pipeline runs in the desired order.

4. **Logging and Monitoring:**
   - Use a logging framework to record essential information about each pipeline run, such as start time, end time, and task statuses.
   - Implement monitoring tools or services to track the progress of the pipeline in real-time and set up alerts for critical issues.

5. **Security:**
   - Securely store API keys and sensitive credentials using a secret management system or environment variables.
   - Encrypt sensitive data both at rest and in transit, especially when storing data in a database.
   - Configure the database to restrict access to authorized users only and regularly update passwords.
