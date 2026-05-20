import requests
import logging
import os
import time
import schedule
from dotenv import load_dotenv
from datetime import datetime, UTC
from google.cloud import bigquery

load_dotenv()


API_KEY = os.getenv("API_KEY")

PROJECT_ID = os.getenv("PROJECT_ID")
DATASET_ID = os.getenv("DATASET_ID")
TABLE_ID = os.getenv("TABLE_ID")

SERVICE_ACCOUNT = os.getenv("SERVICE_ACCOUNT")

logging.basicConfig(
    level=logging.INFO,  
    format="%(asctime)s - %(levelname)s - %(message)s" 
)

cities = ["Hyderabad", "Delhi", "Mumbai", "Chennai"]


def fetch_weather(city):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)

    if response.status_code == 200:
        return response.json()

    else:
        logging.error(f"{city} API Error: {response.status_code}")
        return None


def transform_weather_data(city, data):

    transformed_data = {
        "city": city,
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "weather_condition": data["weather"][0]["main"],
        "timestamp": datetime.now(UTC).isoformat()
    }

    return transformed_data


def load_to_bigquery(client, table_ref, row):

    errors = client.insert_rows_json(table_ref, [row])

    if errors == []:
        logging.info(f"{row['city']} data inserted successfully!")

    else:
        logging.error(f"BigQuery Errors: {errors}")


def run_pipeline():

    try:

        logging.info("Pipeline execution started")

        client = bigquery.Client.from_service_account_json(
            SERVICE_ACCOUNT,
            project=PROJECT_ID
        )

        table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"

        for city in cities:

            logging.info(f"Processing city: {city}")

            raw_data = fetch_weather(city)

            if raw_data:

                transformed_row = transform_weather_data(city, raw_data)

                load_to_bigquery(
                    client,
                    table_ref,
                    transformed_row
                )

        logging.info("Pipeline execution completed")

    except Exception as e:
        logging.exception(f"Pipeline Failed: {e}")


schedule.every(1).minutes.do(run_pipeline)

logging.info("Scheduler started...")

run_pipeline()

while True:

    schedule.run_pending()

    time.sleep(1)