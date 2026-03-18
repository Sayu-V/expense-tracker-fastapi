# Architecture Overview

## 🧾 System Overview

Expense Tracker FastAPI is a modular backend system designed to manage personal finance data such as expenses, categories, budgets, analytics, and reports.

The system follows a **layered + modular architecture**, ensuring:
- Scalability
- Maintainability
- Clean separation of concerns
- Production-readiness

---

## 🏗️ High-Level Architecture

Client (Swagger / Postman)
        ↓
FastAPI Application
        ↓
Routers Layer (API Layer)
        ↓
Service Layer (Business Logic)
        ↓
Storage Layer (In-Memory DB)
        ↓
Response Layer (Schemas)

---

## 📂 Project Structure (Actual)

app/
├── core/
│   ├── dependencies.py
│   ├── exceptions.py
│   └── security.py
│
├── routers/
│   ├── analytics.py
│   ├── budget.py
│   ├── categories.py
│   ├── expenses.py
│   ├── export.py
│   └── reports.py
│
├── schemas/
│   ├── api_responses.py
│   └── expense_schema.py
│
├── services/
│   ├── analytics_service.py
│   ├── expense_service.py
│   └── report_service.py
│
├── storage/
│   └── memory_db.py
│
└── main.py

---

## 🧩 Architecture Layers

### 1. API Layer (Routers)
- Located in: `app/routers/`
- Handles HTTP requests & responses
- Uses FastAPI `APIRouter`
- Contains ~24 endpoints

Responsibilities:
- Input handling
- Calling service layer
- Returning standardized response

---

### 2. Service Layer (Business Logic)
- Located in: `app/services/`
- Core of the application

Handles:
- Expense calculations
- Budget updates
- Analytics processing
- Report generation

✅ Ensures:
- Reusable logic
- Clean separation from API
- Easier testing

---

### 3. Schema Layer (Data Validation & Response)
- Located in: `app/schemas/`

Includes:
- Request validation (Pydantic)
- Response formatting (`APIResponse`)
- Data contracts between layers

---

### 4. Core Layer (Shared Utilities)
- Located in: `app/core/`

Includes:
- Dependencies (DI)
- Custom exceptions
- Security utilities

Purpose:
- Centralized configuration
- Reusable components across modules

---

### 5. Storage Layer (Temporary Data Layer)
- Located in: `app/storage/`

Current Implementation:
- In-memory storage:
  - expenses (list)
  - categories (list)
  - budget (dict)

⚠️ Note:
- No persistence
- Will be replaced by PostgreSQL

---

## 🔄 Request Flow

Client Request
   ↓
Router (API Layer)
   ↓
Service Layer (Business Logic)
   ↓
Memory DB (Storage)
   ↓
Schema (APIResponse)
   ↓
Client Response

---

## ⚙️ Key Architectural Decisions

### 1. Modular Routers
Each feature has its own router:
- expenses
- budget
- analytics
- reports

✔ Improves scalability  
✔ Easier debugging  

---

### 2. Service Layer Separation
Business logic is not inside routers.

✔ Cleaner code  
✔ Better testing  
✔ Industry standard practice :contentReference[oaicite:1]{index=1}  

---

### 3. Centralized Core Layer
- Handles dependencies, exceptions, security

✔ Avoids duplication  
✔ Clean global control  

---

### 4. Schema-driven API
- All responses follow `APIResponse`

✔ Consistent API output  
✔ Frontend-friendly  

---

## 🚧 Current Limitations

- No database (in-memory only)
- No authentication (JWT pending)
- No caching layer
- Limited validation rules
- No async DB operations

---

## 🔮 Future Architecture (Planned)

Client
↓
API Gateway (optional)
↓
FastAPI App
↓
Service Layer
↓
Repository Layer
↓
PostgreSQL Database
↓
Cache (Redis)

---

## 🔐 Planned Enhancements

- JWT Authentication
- Role-based access control
- Rate limiting
- Logging & monitoring
- CI/CD pipeline
- Cloud deployment

---

## 🧠 Architecture Principles Used

- Separation of concerns
- Layered architecture
- Modular design (feature-based routers)
- Dependency injection
- Scalable service-oriented design

---

## 🚀 Architecture Evolution

### 🔹 Phase 1 (Initial)
- Single file (main.py)
- No structure

---

### 🔹 Phase 2 (Current)
- Modular routers
- Service layer added
- Core utilities introduced
- APIResponse standardization
- Docker support
- 24 endpoints

---

### 🔹 Phase 3 (Next)
- Database integration (PostgreSQL)
- Repository layer
- Authentication system
- Production deployment
