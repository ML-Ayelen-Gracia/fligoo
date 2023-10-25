import pandas as pd
from pandas import json_normalize
import requests
import os
from datetime import datetime
import psycopg2
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago

from sqlalchemy import create_engine

# Function to fetch flight data and save to CSV
def fetch_and_save_flight_data():
    # API parameters
    params = {
        'access_key': '6ed36dec9f8ae24519fc54e7e4751678',
        'flight_status': 'active',
        'limit': 100
    }

    # GET request to the API
    api_result = requests.get('http://api.aviationstack.com/v1/flights', params=params)

    api_response = api_result.json()
    api_response_data = api_response['data']

    # Converting data to a DataFrame
    df = pd.DataFrame(api_response_data)

    # Normalizing and selecting columns
    df = json_normalize(api_response_data, errors='ignore')
    selected_columns = [
        'flight_date', 'flight_status', 'departure.airport', 'departure.timezone',
        'arrival.airport', 'arrival.timezone', 'arrival.terminal', 'airline.name', 'flight.number'
    ]
    df = df[selected_columns]

    # Define the directory and file name for saving the CSV
    data_dir = '/mnt/data/source'
    current_date = datetime.now().strftime("%Y-%m-%d")
    table_name = 'test_data'
    csv_filename = f"{data_dir}/{current_date}_{table_name}.csv"

    # Ensure that the data directory exists, or create it if not
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    # Save the DataFrame to a CSV file
    df.to_csv(csv_filename, index=False)
    print(f"DataFrame saved as {csv_filename}")

    # Function to transform flight data
def transform_flight_data():
    # Read the CSV file
    current_date = datetime.now().strftime("%Y-%m-%d")
    table_name = 'test_data'
    csv_filename = f"/mnt/data/source/{current_date}_{table_name}.csv"
    df = pd.read_csv(csv_filename)

    # Replace "/" with " - " in arrival.terminal and departure.timezone
    df['arrival.terminal'] = df['arrival.terminal'].str.replace("/", " - ")
    df['departure.timezone'] = df['departure.timezone'].str.replace("/", " - ")

    # Save the transformed DataFrame back to a CSV file
    if not os.path.exists('/mnt/data/transformed/'):
        os.makedirs('/mnt/data/transformed/')
    transformed_csv_filename = f"/mnt/data/transformed/{current_date}_{table_name}.csv"
    df.to_csv(transformed_csv_filename, index=False)
    print(f"Transformed data saved as {transformed_csv_filename}")


def upload_csv_to_postgresql():
    # PostgreSQL database connection parameters
    db_params = {
        "host": "fligoodb",
        "database": "testfligoo",
        "user": "fligoo",
        "password": "fligoo",
        "port": 5432  # Default PostgreSQL port
    }
    current_date = datetime.now().strftime("%Y-%m-%d")
    table_name = 'test_data'

    csv_file_path = f"/mnt/data/transformed/{current_date}_{table_name}.csv"

    engine = create_engine(f'postgresql+psycopg2://{db_params["user"]}:{db_params["password"]}@{db_params["host"]}:{db_params["port"]}/{db_params["database"]}')

    
    # Read the CSV file into a Pandas DataFrame
    df = pd.read_csv(csv_file_path)
    df = df.rename(columns={
        'departure.airport': 'departure_airport',
        'departure.timezone': 'departure_timezone',
        'arrival.airport': 'arrival_airport',
        'arrival.timezone': 'arrival_timezone',
        'arrival.terminal': 'arrival_terminal',
        'airline.name': 'airline_name',
        'flight.number': 'flight_number'
    })

    table_name = "testdata"
    df.to_sql(table_name, engine, if_exists="replace", index=False)

    print("Data loaded into PostgreSQL table.")

# Function to load data
dag = DAG(
    'flight_data_etl',
    schedule_interval=None,  # Define the schedule interval as needed
    start_date=days_ago(1),
    catchup=False,
    tags=['example'],
)

# Create a PythonOperator to run the fetch_and_save_flight_data function
fetch_flight_data_task = PythonOperator(
    task_id='fetch_flight_data',
    python_callable=fetch_and_save_flight_data,
    dag=dag,
)


transform_flight_data_task = PythonOperator(
    task_id='transform_flight_data',
    python_callable=transform_flight_data,
    dag=dag,
)

upload_csv_to_postgresql_task = PythonOperator(
    task_id='upload_csv_to_postgresql',
    python_callable=upload_csv_to_postgresql,
    dag=dag,
)

fetch_flight_data_task >> transform_flight_data_task
transform_flight_data_task >> upload_csv_to_postgresql_task

