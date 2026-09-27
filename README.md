# 🔗 Linkora

> 💼 A LinkedIn-inspired professional networking platform built with Django.

Linkora is a **professional networking web application** inspired by platforms such as LinkedIn. It provides core features for connecting professionals, sharing posts, exploring job opportunities, and receiving notifications.

## ✨ Features

* 👤 User registration and authentication
* 🧑‍💼 User profiles
* 🤝 Professional connections
* 📝 Create and manage posts
* 💼 Job listings
* 🔔 Notifications
* 📁 Media and file handling
* 🗄️ SQLite database for development
* 🐳 Docker & Docker Compose support

## 🛠️ Tech Stack

| Technology            | Purpose                    |
| --------------------- | -------------------------- |
| 🐍 **Python**         | Programming language       |
| 🌐 **Django**         | Web framework              |
| 🗄️ **SQLite**        | Development database       |
| 🐳 **Docker**         | Containerization           |
| 📦 **Docker Compose** | Multi-container management |

## 📂 Project Structure

```text
Linkora/
├── 👤 accounts/          # User accounts and profiles
├── 🤝 connections/       # Professional connections
├── 💼 jobs/              # Job-related functionality
├── 🔔 notifications/     # User notifications
├── 📝 posts/             # Posts and social interactions
├── ⚙️ core/              # Core project configuration
├── 📁 media/             # Uploaded media files
├── 🐳 Dockerfile
├── 🐳 docker-compose.yml
├── ⚙️ manage.py
└── 📦 requirements.txt
```

## 🚀 Getting Started

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Heroid-Dev/Linkora.git
cd Linkora
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
```

Activate it on **Linux/macOS**:

```bash
source venv/bin/activate
```

On **Windows**:

```bash
venv\Scripts\activate
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run Migrations

```bash
python manage.py migrate
```

### 5️⃣ Start the Development Server

```bash
python manage.py runserver
```

🌐 The application will be available at:

```text
http://127.0.0.1:8000/
```

## 🐳 Docker

Linkora also includes Docker configuration for easier development and deployment.

Run the project using Docker Compose:

```bash
docker compose up --build
```

## 🎯 Project Goals

The main goal of Linkora is to practice building a **real-world web application with Django** and gain hands-on experience with the architecture and implementation of professional social networking platforms.

Through this project, the following areas are explored:

* 🏗️ Django project architecture
* 🔐 Authentication and user management
* 🤝 Social connections
* 📝 Content management
* 💼 Job management
* 🔔 Notification systems
* 🐳 Containerized development

## 🔮 Future Improvements

* 🚀 REST API with Django REST Framework
* 🔎 Advanced search and filtering
* 🤖 Recommendation system
* ⚡ Real-time notifications
* 🐘 PostgreSQL support
* 🔴 Redis & Celery integration
* 🧪 Automated testing
* ☁️ Production deployment configuration

## 📌 Project Status

🚧 **Linkora is currently under development.**

This project is primarily developed for **learning, experimentation, and portfolio purposes**.

## 📄 License

This project is intended for **educational and portfolio purposes**.
