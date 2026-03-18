# 🧩 Low Level Design (LLD)

## 📌 Overview

This document describes the detailed internal structure of the Expense Tracker FastAPI application, including modules, data models, API endpoints, and request handling.

The system follows a **layered architecture**:

Router → Service → Storage → Schema → Response

---

## 📂 Module Breakdown

### 1. Entry Point

#### `main.py`
- Initializes FastAPI application
- Registers routers
- Configures middleware and dependencies
- Acts as the composition layer (no business logic)

---

### 2. Core Layer (`app/core/`)

#### `dependencies.py`
- Handles dependency injection
- Used for shared resources (future DB/session)

#### `exceptions.py`
- Custom exception handling
- Centralized error management

#### `security.py`
- Security utilities (future JWT/auth support)

---

### 3. API Layer (`app/routers/`)

Handles HTTP requests using FastAPI `APIRouter`.

#### Modules:
- `expenses.py`
- `categories.py`
- `budget.py`
- `analytics.py`
- `reports.py`
- `export.py`

Responsibilities:
- Define endpoints
- Validate inputs via schemas
- Call service layer
- Return standardized responses

---

### 4. Service Layer (`app/services/`)

Contains business logic and computation.

#### Modules:
- `expense_service.py`
- `analytics_service.py`
- `report_service.py`

Responsibilities:
- Expense processing
- Budget calculations
- Filtering & searching
- Analytics computation
- Report generation

---

### 5. Schema Layer (`app/schemas/`)

Defines request and response models using **Pydantic**.

#### Files:
- `api_responses.py`
- `expense_schema.py`

Responsibilities:
- Input validation
- Data serialization
- API response standardization

---

### 6. Storage Layer (`app/storage/`)

#### `memory_db.py`

In-memory data store:

```python
categories = []
expenses = []
budget = {}
```
Responsibilities:

Temporary data persistence

Simulates database behavior

## 🧾 Data Models
Expense Model
Field	Type	Description
id	int	Unique identifier
category	str	Expense category
amount	float	Expense amount
note	str	Optional description
date	str	Expense date

## Category Model
Field	Type	Description
id	int	Unique identifier
name	str	Category name

## Budget Model
Field	Type	Description
limit	float	Budget limit
spent	float	Total expenses spent

## 🔌 API Endpoints
## 🧾 Expenses
- GET /expenses → Get all expenses
- POST /expenses → Create expense
- GET /expenses/{id} → Get expense by ID
- PUT /expenses/{id} → Update expense
- DELETE /expenses/{id} → Delete expense

## 🏷️ Categories
- GET /categories → List categories
- POST /categories → Add category
- DELETE /categories/{id} → Delete category

## 💰 Budget

- POST /budget → Set budget
- GET /budget → Get budget
- GET /budget/status → Budget usage

## 📊 Analytics

## GET /analytics/category → Category-wise analytics
- GET /analytics/monthly → Monthly trends

## 📈 Reports
- GET /reports/summary → Overall summary
- GET /reports/category → Category summary

## 📤 Export
- GET /export/csv → Export data as CSV

## 🔍 Filters & Search
- GET /expenses/filter/category
- GET /expenses/filter/date
- GET /expenses/filter/amount
- GET /expenses/search

## 🔄 Request Handling Flow
1. Client sends HTTP request
2. Router receives request
3. Input validated via Pydantic schema
4. Service layer processes logic
5. Data retrieved/updated in memory DB
6. Response formatted using APIResponse
7. JSON response returned to client

## ✅ Validation Strategy

Implemented using Pydantic models
Ensures:
- Correct data types
- Required fields
- Structured request/response format
- FastAPI automatically validates request data and serializes responses based on schema definitions

## ⚠️ Error Handling
- Centralized via core/exceptions.py
- Returns consistent error responses
- Prevents unhandled exceptions

## 🚧 Current Limitations
- No persistent database
- No authentication/authorization
- Limited validation rules
- No caching mechanism

## 🔮 Future Enhancements

- PostgreSQL integration
- Repository layer addition
- JWT authentication
- Advanced filtering & pagination
- Async database operations
