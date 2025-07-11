# 📂 Distributed File Ingestion System

A scalable, containerized file ingestion backend with S3 upload support, Prometheus monitoring, Grafana visualization, and CI/CD deployment using GitHub Actions & Docker Hub.

## 🚀 Live Demo

🔗 [https://distributed-ingestion-backend.onrender.com](https://distributed-ingestion-backend.onrender.com)

> Note: The backend supports file uploads via `/upload` endpoint. Use Postman or cURL to test.

---

## 🧩 Key Features

- ⚡ Concurrent file uploads to **AWS S3**
- 🧠 Lightweight **Flask API** with SQLite tracking
- 📈 Real-time **Prometheus metrics** exposed at `/metrics`
- 📊 Dashboards powered by **Grafana**
- 🐳 Dockerized application with `docker-compose`
- 🔁 Fully automated **CI/CD pipeline** via GitHub Actions
- 🔐 Secret management with GitHub Actions Secrets

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask, SQLite
- **Cloud Storage**: AWS S3
- **Containerization**: Docker, Docker Compose
- **Monitoring**: Prometheus, Grafana
- **CI/CD**: GitHub Actions, Docker Hub
- **Deployment**: Render.com (Free Tier)

---

## ⚙️ Setup Instructions

### 1. 🔧 Clone the Repository

```bash
git clone https://github.com/yourusername/distributed-ingestion-system.git
cd distributed-ingestion-system

### 2. 🧪 Run Locally (with Python)

