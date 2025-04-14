# 🚦 Real-Time  ETL of Road Traffic & Weather Monitoring.

> 🛰️ An end-to-end real-time data engineering pipeline to collect, process, and visualize road traffic & weather data using **Kafka**, **Airflow**, **PostgreSQL**, and **Grafana Loki**—fully containerized with **Docker**.

---
---

## 📚 Table of Contents
- [Overview](#-overview)
- [Key Features](#-features)
- [Tech Stack](#-tech-stack)
- [Getting Started](#-GettingStarted)
- [Prerequisites](#-Prerequisites)
- [Credentials & API Key Handling](#-credentials--api-keys)
- [Screenshots](#-screenshots)

<a href="[https://www.example.com](https://www.canva.com/design/DAGh5KDbTKQ/y8tjSorL17l5vWz83W6nQQ/watch)">Visit Example</a>

## 🔑 Key Features


  <iframe loading="lazy" style="position: absolute; width: 100%; height: 100%; top: 0; left: 0; border: none; padding: 0;margin: 0;"
    src="https://www.canva.com/design/DAGh5KDbTKQ/y8tjSorL17l5vWz83W6nQQ/watch?embed" allowfullscreen="allowfullscreen" allow="fullscreen">
  </iframe>
<a href="https:&#x2F;&#x2F;www.canva.com&#x2F;design&#x2F;DAGh5KDbTKQ&#x2F;y8tjSorL17l5vWz83W6nQQ&#x2F;watch?utm_content=DAGh5KDbTKQ&amp;utm_campaign=designshare&amp;utm_medium=embeds&amp;utm_source=link" target="_blank" rel="noopener">docker pull &lt;image_name&gt;:&lt;tag&gt;</a> by ANIMESH SINGH


- **🐳 Fully Dockerized Architecture**  
  Deploy the entire stack with a single `docker-compose up --build` — no manual setup.

- **⚙️ Real-Time ETL Pipeline with Kafka Streaming**  
  Data is streamed in real-time using Apache Kafka, then processed via Python-based ETL jobs and stored in PostgreSQL.

- **⏰ Airflow-Based Workflow Orchestration**  
  Apache Airflow schedules and manages ETL workflows and task dependencies.
  
- **📡 Apache Kafka for High-Throughput Streaming**  
  Handles real-time data ingestion and decoupling between data producers and consumers.

- **📝 Centralized Logging with Loki**  
  All logs from Python apps and Airflow tasks are sent to Grafana Loki for monitoring and troubleshooting.

- **📊 Visual Monitoring with Grafana**  
  Dashboards offer real-time insights into pipeline performance, traffic flow, and logs.

- **🔔 Notification System (Optional)**  
  Sends ETL job alerts (success/failure) via Discord webhooks.

- **🔐 Secure Credential & API Key Management**  
  Firebase securely stores API keys, secrets, and credentials — no hardcoding.

- **💾 Persistent PostgreSQL Storage**  
  Maintains structured data and ensures durability across restarts.

- **📁 Configurable & Extensible**  
  Clean modular structure with support for external config files, secrets, and new data sources.

- **👨‍💻 Plug-and-Play for Recruiters**  
  Instantly clonable and runnable — ideal for technical demos or code evaluations.

---
# 🛠️ Tech stack

| Component      | Tool / Service        | Logo                              |
|----------------|-----------------------|-----------------------------------|
| **Data Source** | TomTom, Overpass, WeatherAPI | <img src="https://upload.wikimedia.org/wikipedia/commons/c/c1/Tomtom_logo.jpg" alt="TomTom" width="50"/> <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/b0/Openstreetmap_logo.svg/225px-Openstreetmap_logo.svg.png" alt="Overpass" width="50"/> <img src="https://openweathermap.org/themes/openweathermap/assets/img/logo_white_cropped.png" alt="WeatherAPI" width="50"/> |
| **Scheduler**  | Apache Airflow         | <img src="https://icon.icepanel.io/Technology/svg/Apache-Airflow.svg" alt="Airflow" width="70"/> |
| **Streaming**  | Apache Kafka           | <img src="https://irisidea.com/wp-content/uploads/2024/04/kafka-implementation-experience--450x231.png" alt="Kafka" width="120"/> |
| **Storage**    | PostgreSQL             | <img src="https://www.logo.wine/a/logo/PostgreSQL/PostgreSQL-Logo.wine.svg" alt="PostgreSQL" width="120"/> |
| **Logging**    | Grafana Loki           | <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a1/Grafana_logo.svg/2005px-Grafana_logo.svg.png" alt="Grafana Loki" width="100"/> |
| **UI framework**    | Streamlit           | <img src="https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png" alt="Streamlit" width="180"/> |
| **Containerization**  | Docker, Docker Compose | <img src="https://cdn4.iconfinder.com/data/icons/logos-and-brands/512/97_Docker_logo_logos-1024.png" alt="Docker" width="100"/>|
| **API & Credentials**   | Firebase               | <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTxQktpK3Jy3GkxXutGPzl8R3OBCNMxfFWP5A&s" alt="Firebase" width="130"/>|
| **Alerts and other**   | Discord               | <img src="https://pngimg.com/uploads/discord/discord_PNG3.png" alt="Discord" width="110"/>|
| **Language**   | Python                 | <img src="https://s3.dualstack.us-east-2.amazonaws.com/pythondotorg-assets/media/community/logos/python-logo-only.png" alt="Python" width="70"/>|

---

# 🚀 Getting Started

## ⚠️ IMPORTANT

<p align="center">
  <img src="https://img.freepik.com/free-vector/www-concept-illustration_114360-2143.jpg?t=st=1744565213~exp=1744568813~hmac=cc0420ee0ca016a8962950768146a9a73c652ef7e93dfd0f6be86f2c3eca7cb6&w=826" alt="API Status" width="300"/>
</p>

> Before cloning and running this project, **please ensure that the API is up and running.**

🔗 **[Visit Project App](https://traffic-api-status.vercel.app/?show_api=1#)**  
Make sure the API is **not down** before proceeding.

💡 Once the API is confirmed to be **live and functional**, you can go ahead and clone the repo, and run the project locally. 
Just follow the steps below 👇


## ✅ Prerequisites

Before running this project locally, make sure you have the following installed on your system:

- [Docker](https://www.docker.com/products/docker-desktop) & [Docker Compose](https://docs.docker.com/compose/)
- [Git](https://git-scm.com/downloads)
- A code editor like [VS Code](https://code.visualstudio.com/)
- Internet connection to access external APIs (TomTom, WeatherAPI, etc.)

💡 **Note:**  
Ensure that your system’s firewall or antivirus isn’t blocking Docker containers from making network requests.


###  Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/animesh11singh/project_real_time_trafic_monitoring.git
cd project_real_time_trafic_monitoring
```



### 📂 Folder Structure

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



### Run in terminal

```bash
docker-compose up -d --build
```

### ▶️ Next Steps

Once the project is up and running, follow these steps:

1. 🌐 Open your browser and visit:  
   **[http://localhost:8501/](http://localhost:8501/)**  
   This will open the ETL helper streamlit app .

2. 📋 **Follow the ETL instructions** provided on the dashboard to get started.

3. 🐳 **Keep an eye on your containers:**  
   Use `docker ps` or Docker Desktop to monitor the status of all services.

---

✅ Everything running smoothly? You're all set to explore the project!


## Access the Services

Once the containers are up and running, you can access the following services through your browser:

| Service           | URL                           | Username | Password |
|-------------------|-------------------------------|----------|----------|
| Streamlit App     | [http://localhost:8501](http://localhost:8501) | _N/A_     | _N/A_     |
| Airflow UI        | [http://localhost:8080](http://localhost:8080) | `animesh` | `animesh16` |
| Grafana Dashboard | [http://localhost:3000](http://localhost:3000) | `admin`   | `animesh16` or `admin`   |

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
