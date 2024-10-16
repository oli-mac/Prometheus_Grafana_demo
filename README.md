

# Observability Stack with FastAPI, Prometheus, Loki, and Grafana

This project provides a basic setup for an observability stack using FastAPI, Prometheus, Loki, and Grafana. It includes a simple FastAPI application, a Docker Compose file for easy deployment, and a Dockerfile for building the application image.

## Table of Contents

* [Prerequisites](#prerequisites)
* [Setup Instructions](#setup-instructions)
* [Components](#components)
* [Configuration](#configuration)
* [Usage](#usage)
* [Troubleshooting](#troubleshooting)

## Prerequisites

* Docker and Docker Compose installed on your system
* Python 3.9 or later
* PostgreSQL database (optional)

## Setup Instructions

1. Clone this repository to your local machine.
2. Create a new directory for your project and navigate into it.
3. Copy the `docker-compose.yml` and `Dockerfile` files from this repository into your project directory.
4. Create a new file named `main.py` and copy the contents of the `main.py` file from this repository into it.
5. Create a new file named `prometheus.yml` and copy the contents of the `prometheus.yml` file from this repository into it.
6. Create a new file named `promtail-config.yaml` and copy the contents of the `promtail-config.yaml` file from this repository into it.
7. Create a new file named `loki-config.yaml` and copy the contents of the `loki-config.yaml` file from this repository into it.
8. Run `docker-compose up -d` to start the containers in detached mode.

## Components

* **FastAPI Application**: The `main.py` file contains a simple FastAPI application that exposes a single endpoint for creating text entries.
* **Prometheus**: The `prometheus.yml` file configures Prometheus to scrape metrics from the FastAPI application.
* **Loki**: The `loki-config.yaml` file configures Loki to collect logs from the FastAPI application.
* **Grafana**: The `docker-compose.yml` file includes a Grafana service that can be used to visualize metrics and logs.
* **PostgreSQL Database**: The `docker-compose.yml` file includes a PostgreSQL database service that can be used to store data.

## Configuration

* **Environment Variables**: The `docker-compose.yml` file sets environment variables for the FastAPI application, including `DATABASE_URL`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, and `POSTGRES_DB`.
* **Prometheus Configuration**: The `prometheus.yml` file configures Prometheus to scrape metrics from the FastAPI application.
* **Loki Configuration**: The `loki-config.yaml` file configures Loki to collect logs from the FastAPI application.
* **Grafana Configuration**: The `docker-compose.yml` file includes a Grafana service that can be configured to visualize metrics and logs.

## Usage

* **Create Text Entries**: Use the `create_text` endpoint to create new text entries.
* **View Metrics**: Use the Grafana dashboard to view metrics from the FastAPI application.
* **View Logs**: Use the Grafana dashboard to view logs from the FastAPI application.

## Troubleshooting

* **Check Container Logs**: Use `docker-compose logs` to view logs from the containers.
* **Check Prometheus Metrics**: Use the Prometheus dashboard to view metrics from the FastAPI application.
* **Check Loki Logs**: Use the Loki dashboard to view logs from the FastAPI application.