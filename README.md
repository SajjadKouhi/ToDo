# 📌 ToDo Project

## 📖 Introduction
This is a **Django REST Framework** based **To-Do List API**, allowing users to manage their tasks efficiently. The project supports user authentication, task creation, completion, and deletion.

## 🛠️ Technologies Used
- **Python** (Django, Django REST Framework)
- **SQLite** (Database)
- **Docker & Docker Compose** (Containerization)
- **Git & GitHub** (Version Control)

## 🚀 Features
- User authentication (Registration & Login with JWT)
- CRUD operations for tasks
- Marking tasks as completed
- Categorizing tasks
- API secured with authentication

## 📦 Installation

### 1️⃣ Clone the Repository
```bash
$ git clone https://github.com/SajjadKouhi/ToDo.git
$ cd ToDo
```

### 2️⃣ Create Virtual Environment & Install Dependencies
```bash
$ python -m venv venv
$ source venv/bin/activate   # On Windows use: venv\Scripts\activate
$ pip install -r requirements.txt
```

### 3️⃣ Apply Migrations & Run Server
```bash
$ python manage.py migrate
$ python manage.py runserver
```

## 🐳 Running with Docker

### 1️⃣ Build the Docker Image
```bash
$ docker-compose build
```

### 2️⃣ Run the Containers
```bash
$ docker-compose up -d
```

### 3️⃣ Stop Containers
```bash
$ docker-compose down
```

## 🔥 API Endpoints

### Authentication
| Method | Endpoint               | Description             |
|--------|------------------------|-------------------------|
| POST   | `/user/register/`       | Register a new user    |
| POST   | `/user/login/`          | Login and get JWT      |

### Tasks Management
| Method | Endpoint                 | Description                     |
|--------|--------------------------|---------------------------------|
| POST   | `/tasks/`                 | Create a new task              |
| GET    | `/tasks/`                 | List all tasks of a user       |
| PATCH  | `/tasks/<task_id>/`       | Update task details            |
| DELETE | `/tasks/<task_id>/`       | Delete a task                  |
| PUT    | `/tasks/completed/<task_id>/` | Mark task as completed   |

## 🔗 Contributing
Feel free to contribute! Fork the repo, make your changes, and submit a pull request. 😊

## 📄 License
This project is open-source and available under the **MIT License**.

---
💡 Developed by **Sajjad Kouhi**

