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
| **Data Source** | TomTom, Overpass, WeatherAPI | <img src="https://upload.wikimedia.org/wikipedia/commons/c/c1/Tomtom_logo.jpg" alt="TomTom" width="50"/> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Openstreetmap_logo.svg/225px-Openstreetmap_logo.svg.png" alt="Overpass" width="50"/> <img src="https://openweathermap.org/themes/openweathermap/assets/img/logo_white_cropped.png" alt="WeatherAPI" width="50"/> |
| **Scheduler**  | Apache Airflow         | <img src="https://icon.icepanel.io/Technology/svg/Apache-Airflow.svg" alt="Airflow" width="80"/> |
| **Streaming**  | Apache Kafka           | <img src="https://irisidea.com/wp-content/uploads/2024/04/kafka-implementation-experience--450x231.png" alt="Kafka" width="100"/> |
| **Storage**    | PostgreSQL             | <img src="https://www.logo.wine/a/logo/PostgreSQL/PostgreSQL-Logo.wine.svg" alt="PostgreSQL" width="100"/> |
| **Logging**    | Grafana Loki           | <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Grafana_logo.svg/2005px-Grafana_logo.svg.png" alt="Grafana Loki" width="100"/> |
| **Container**  | Docker, Docker Compose | <img src="https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/97_Docker_logo_logos-1024.png" alt="Docker" width="100"/>|
| **Language**   | Python                 | <img src="https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/community/logos/python-logo-only.png" alt="Python" width="100"/>|

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
