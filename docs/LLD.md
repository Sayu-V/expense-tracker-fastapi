# Low Level Design (LLD)

## Modules

main.py

Contains FastAPI application and API endpoints.

---

# Expense Data Model

Expense

id
category
amount
note
date

---

# API Endpoints

Expenses

GET /expenses
POST /expenses
GET /expenses/{id}
PUT /expenses/{id}
DELETE /expenses/{id}

Categories

GET /categories
POST /categories
DELETE /categories/{id}

Budget

POST /budget
GET /budget
GET /budget/status

Reports

GET /summary
GET /summary/category

Export

GET /export/csv

---

# Request Validation

Input validation is performed using **Pydantic models**.

This ensures:

* correct data types
* required fields
* structured API requests
