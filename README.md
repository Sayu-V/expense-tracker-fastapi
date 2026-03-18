# 🚀 Expense Tracker API (FastAPI)

A scalable backend REST API for managing personal finance data such as expenses, categories, budgets, analytics, and reports.

Built using **FastAPI**, **Python**, and **Docker**, this project demonstrates a **modular, service-based backend architecture** used in real-world applications.

---

## ✨ Features

- Expense CRUD operations
- Category management
- Budget tracking
- Expense filtering & search
- Analytics & reports
- CSV export functionality
- Standardized API responses
- Modular router-based architecture
- Swagger API documentation

---

## 🏗️ Architecture Highlights

- Modular routing using FastAPI `APIRouter`
- Service layer for business logic separation
- Centralized core utilities (dependencies, exceptions, security)
- Schema-based request/response validation
- In-memory storage (replaceable with DB)

📌 This follows modern FastAPI best practices like:
- Thin routers + service layer logic  
- Modular feature-based design  
- Clean separation of concerns :contentReference[oaicite:0]{index=0}  

---

## 🛠️ Tech Stack

| Component        | Technology        |
|------------------|------------------|
| Language         | Python           |
| API Framework    | FastAPI          |
| Validation       | Pydantic         |
| Architecture     | Layered + Modular|
| Containerization | Docker           |
| API Docs         | Swagger / OpenAPI|
| Storage (Current)| In-memory        |
| Future DB        | PostgreSQL       |

---

## 📂 Project Structure
app/
├── core/ # Shared utilities (security, exceptions, dependencies)
├── routers/ # API endpoints (feature-based)
├── services/ # Business logic layer
├── schemas/ # Request/response models
├── storage/ # In-memory database
└── main.py # Entry point

docs/
├── ARCHITECTURE.md
├── HLD.md
├── LLD.md
└── tech-stack.md

Dockerfile
docker-compose.yml
requirements.txt


---

## 🔄 Request Flow

Client → Router → Service → Storage → APIResponse → Client

---

## ▶️ Running the Project

### 1. Start using Docker

```bash
docker compose up --build

2. Access API Docs

Swagger UI:

http://localhost:8000/docs
📊 API Overview

~24 REST endpoints

Organized by modules:

expenses

categories

budget

analytics

reports

export

🧪 Testing

You can test APIs using:

Swagger UI

Postman

Example:

GET /expenses
POST /expenses
GET /analytics
🚧 Current Limitations

No persistent database (in-memory only)

No authentication system (JWT pending)

No caching layer

Limited validation rules

🔮 Future Improvements

PostgreSQL integration

Repository layer

JWT Authentication

User management

Redis caching

Cloud deployment (AWS/GCP)

CI/CD pipeline

See PROJECT_ROADMAP.md for details.

📘 API Documentation

FastAPI automatically generates interactive docs:

Swagger UI:

http://localhost:8000/docs
🤝 Contributing

Contributions are welcome!

Please check:

CONTRIBUTING.md
📜 License

MIT License

---
