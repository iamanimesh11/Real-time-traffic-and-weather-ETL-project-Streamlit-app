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

<h2>🛠️ Technologies Used</h2>
<div style="display: flex; flex-wrap: wrap; gap: 1rem;">
  <div style="flex: 1 1 300px; padding: 1rem; border: 1px solid #ddd; border-radius: 8px;">
    <strong>📡 Data Source:</strong> TomTom, Overpass, WeatherAPI
  </div>
  <div style="flex: 1 1 300px; padding: 1rem; border: 1px solid #ddd; border-radius: 8px;">
    <strong>⏰ Scheduler:</strong> Apache Airflow
  </div>
  <div style="flex: 1 1 300px; padding: 1rem; border: 1px solid #ddd; border-radius: 8px;">
    <strong>🔄 Streaming:</strong> Apache Kafka
  </div>
  <div style="flex: 1 1 300px; padding: 1rem; border: 1px solid #ddd; border-radius: 8px;">
    <strong>🗄️ Storage:</strong> PostgreSQL
  </div>
  <div style="flex: 1 1 300px; padding: 1rem; border: 1px solid #ddd; border-radius: 8px;">
    <strong>📊 Logging:</strong> Grafana Loki
  </div>
  <div style="flex: 1 1 300px; padding: 1rem; border: 1px solid #ddd; border-radius: 8px;">
    <strong>📦 Container:</strong> Docker, Docker Compose
  </div>
  <div style="flex: 1 1 300px; padding: 1rem; border: 1px solid #ddd; border-radius: 8px;">
    <strong>🐍 Language:</strong> Python
  </div>
</div>

---

## 🚀 Getting Started

### Prerequisites

- Docker & Docker Compose
- Python 3.8+
- Kafka, PostgreSQL, Grafana Loki (automated with Docker)

### Run Services

```bash
docker-compose up -d
```

### Run Airflow

```bash
# Inside airflow/
airflow standalone
```

### Run Kafka

```bash
# Run Producer
python kafka/producer.py

# Run Consumer
python kafka/consumer.py
```

---

## 🗃️ Data Stored

| Table Name       | Description                      |
|------------------|----------------------------------|
| roads_traffic     | Road metadata from Overpass API |
| traffic_flow_data | Real-time traffic speed data    |
| weather_conditions| Weather data per coordinate     |

---

## 📊 Future Scope

- Integrate Spark or PySpark to process stored JSON data
- Build ML model to predict traffic congestion
- Expose API via FastAPI or Flask to serve predictions
- Visualize insights with Power BI / Tableau

---

## 👤 Author

- **[Your Name]**
- 💼 Aspiring Data Engineer | Python | Kafka | Airflow | Docker
```

----------------------------------------------------------------------------
