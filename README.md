# Weather API ETL Pipeline using GCP BigQuery

## Project Overview

This project is an end-to-end Data Engineering ETL pipeline built using Python and Google Cloud Platform (GCP).

The pipeline fetches real-time weather data from the OpenWeather API for multiple cities, transforms the data, and loads it into Google BigQuery for analytics.

The project also includes:

* Multi-city batch processing
* Modular ETL architecture
* Logging and exception handling
* Environment variable management
* Automated scheduling
* Partitioned and clustered BigQuery tables

---

# Architecture

```text
Weather API
     ↓
Python ETL Pipeline
     ↓
Data Transformation
     ↓
BigQuery Data Warehouse
     ↓
SQL Analytics
```

---

# Technologies Used

| Technology                  | Purpose                         |
| --------------------------- | ------------------------------- |
| Python                      | ETL development                 |
| Google BigQuery             | Data warehouse                  |
| OpenWeather API             | Weather data source             |
| Google Cloud Platform (GCP) | Cloud platform                  |
| Logging                     | Monitoring and debugging        |
| Schedule Library            | Pipeline automation             |
| dotenv                      | Environment variable management |

---

# Features

* Fetches weather data for multiple cities
* Performs ETL processing
* Transforms nested JSON data into structured records
* Loads data into BigQuery
* Uses partitioned BigQuery tables
* Uses clustered BigQuery tables
* Includes logging and error handling
* Supports scheduled batch processing
* Uses secure environment variable configuration

---

# ETL Workflow

## Extract

* Fetches weather data from OpenWeather API using Python requests library.

## Transform

* Parses nested JSON response
* Extracts required fields
* Creates structured records
* Adds timestamps

## Load

* Loads transformed records into BigQuery using Python BigQuery client.

---

# BigQuery Table Design

## Dataset

```text
weather_analytics
```

## Table

```text
weather_data
```

## Schema

| Column            | Type      |
| ----------------- | --------- |
| city              | STRING    |
| temperature       | FLOAT     |
| humidity          | INTEGER   |
| weather_condition | STRING    |
| timestamp         | TIMESTAMP |

---

# BigQuery Optimizations

## Partitioning

Partitioned by:

```text
timestamp
```

Partition type:

```text
By Day
```

## Clustering

Clustered by:

```text
city
```

---

# Project Structure

```text
weather-pipeline/
│
├── main.py
├── config.py
├── requirements.txt
├── .env
├── .gitignore
├── credentials/
│   └── weather-bigquery-sa.json
```

---

# Environment Variables

Create a `.env` file:

```env
API_KEY=YOUR_API_KEY

PROJECT_ID=weather-data-pipeline-495616
DATASET_ID=weather_analytics
TABLE_ID=weather_data

SERVICE_ACCOUNT=credentials/weather-bigquery-sa.json
```

---

# Installation Steps

## Clone Repository

```bash
git clone <repository-url>
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac/Linux

```bash
source venv/bin/activate
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Pipeline

## Manual Execution

```bash
python main.py
```

## Scheduled Execution

The pipeline automatically runs every minute using the Python schedule library.

---

# Sample SQL Queries

## View All Records

```sql
SELECT *
FROM `weather-data-pipeline-495616.weather_analytics.weather_data`
```

## Average Temperature

```sql
SELECT AVG(temperature) AS avg_temperature
FROM `weather-data-pipeline-495616.weather_analytics.weather_data`
```

## Weather Condition Counts

```sql
SELECT
    weather_condition,
    COUNT(*) AS total_records
FROM `weather-data-pipeline-495616.weather_analytics.weather_data`
GROUP BY weather_condition
```

## Daily Temperature Trends

```sql
SELECT
    DATE(timestamp) AS weather_date,
    AVG(temperature) AS avg_temp
FROM `weather-data-pipeline-495616.weather_analytics.weather_data`
GROUP BY weather_date
ORDER BY weather_date
```

---

# Logging and Error Handling

The pipeline includes:

* INFO logs for successful execution
* ERROR logs for failures
* Exception handling using try/except
* API validation using HTTP status codes

---

# Security Best Practices

* API keys stored in `.env`
* Service account keys excluded using `.gitignore`
* Credentials not hardcoded in source code

---

# Future Improvements

Possible enhancements:

* Cloud Functions deployment
* Cloud Scheduler automation
* Apache Airflow orchestration
* Real-time streaming using Pub/Sub
* Dashboard creation using Looker Studio
* CI/CD integration

---

# Key Data Engineering Concepts Used

* ETL Pipeline
* Batch Processing
* API Ingestion
* JSON Transformation
* Data Warehousing
* Partitioning
* Clustering
* Scheduling
* Logging
* Exception Handling
* Environment Variables

---

# Resume Highlights

* Built an automated ETL pipeline using Python and GCP BigQuery.
* Implemented multi-city batch processing using REST APIs.
* Designed partitioned and clustered BigQuery tables for optimized analytics.
* Added logging, exception handling, and modular ETL architecture.
* Automated pipeline execution using Python scheduler.

---

# Author

Vinay Kumar
