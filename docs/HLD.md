# High Level Design (HLD)

## System Overview

Expense Tracker API is a backend system designed to manage personal expense records through a REST API.

The system allows users to:

* record expenses
* categorize spending
* generate summaries
* analyze spending patterns

---

# System Architecture

Client Application
↓
FastAPI REST API
↓
Business Logic Layer
↓
Data Storage Layer

Future architecture:

Client
↓
FastAPI
↓
SQLModel ORM
↓
PostgreSQL Database

---

# Key Components

API Layer

Handles HTTP requests and responses.

Business Logic Layer

Processes expense calculations and analytics.

Data Layer

Stores expense data.

---

# Deployment Architecture

Docker Container

Runs the FastAPI backend service.

Future deployment may include:

* PostgreSQL container
* cloud deployment
* CI/CD pipelines
