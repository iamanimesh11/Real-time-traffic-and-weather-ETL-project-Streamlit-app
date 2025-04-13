# 🚦 Real-Time  ETL of Road Traffic & Weather Monitoring.

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
# 🛠️ Technologies Used

| Component      | Tool / Service        | Logo                              |
|----------------|-----------------------|-----------------------------------|
| **Data Source** | TomTom, Overpass, WeatherAPI | ![TomTom Logo](https://example.com/tomtom-logo.png) ![Overpass Logo](https://example.com/overpass-logo.png) ![WeatherAPI Logo](https://example.com/weatherapi-logo.png) |
| **Scheduler**  | Apache Airflow         | ![Airflow Logo](https://icon.icepanel.io/Technology/svg/Apache-Airflow.svg) |
| **Streaming**  | Apache Kafka           | ![Kafka Logo](https://kafka.apache.org/images/apache-kafka.png) |
| **Storage**    | PostgreSQL             | ![PostgreSQL Logo](https://example.com/postgresql-logo.png) |
| **Logging**    | Grafana Loki           | ![Grafana Loki Logo](https://www.skedler.com/blog/wp-content/uploads/2021/08/grafana-logo-768x384.png) |
| **Container**  | Docker, Docker Compose | ![Docker Logo](https://example.com/docker-logo.png) ![Docker Compose Logo](https://example.com/docker-compose-logo.png) |
| **Language**   | Python                 | ![Python Logo](https://example.com/python-logo.png) |

---

# 🚀 Getting Started

## ⚠️ IMPORTANT:

Before cloning and running this project, **_please ensure that the API is up and running_**. 

➡️ **Visit my website** and confirm that the API is not down. If the API is up and functional, then you can proceed with cloning the repository and running the project.

### 🔗 **Visit Project App**:  
> _**https://traffic-api-status.vercel.app/?show_api=1#**_

💡 **To get this project up and running on your local machine, follow these simple steps:**
<img src="https://icon.icepanel.io/Technology/svg/Apache-Airflow.svg" alt="API Status" width="400"/>



###  Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/animesh11singh/project_real_time_trafic_monitoring.git
cd project_real_time_trafic_monitoring
```



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

```




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
