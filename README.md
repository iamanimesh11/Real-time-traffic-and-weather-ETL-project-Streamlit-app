# 🚦 Real-Time Road Traffic & Weather Monitoring System

An end-to-end real-time data engineering pipeline to collect, process, and visualize traffic & weather data using **Kafka**, **Airflow**, **PostgreSQL**, and **Grafana Loki**—fully containerized with **Docker**.

---

## 📌 Key Features

- 🔄 Real-time traffic flow via [TomTom API](https://developer.tomtom.com/)
- 🌐 Nearby road extraction using Overpass API (OpenStreetMap)
- 🌦️ Weather data integration from [WeatherAPI](https://www.weatherapi.com/)
- ⚙️ Kafka Producer/Consumer for scalable streaming
- 📅 Task orchestration via Apache Airflow DAGs
- 🗃️ PostgreSQL for structured storage
- 📈 Grafana Loki for centralized logging
- 🐳 Dockerized for easy deployment

---

## 📂 Folder Structure

```bash
.
├── airflow/                 # DAGs & Airflow configs
│   └── dags/
│       └── traffic_pipeline_dag.py
├── kafka/
│   ├── producer.py          # Traffic/Weather fetch
│   └── consumer.py          # DB insertion
├── scripts/
│   ├── get_nearby_roads.py  # Overpass API call
│   ├── transform_traffic.py
│   └── bulk_insert.py
├── grafana_loki/
│   └── loki-config.yaml
├── postgres/
│   └── init.sql
├── docker-compose.yml
└── README.md
