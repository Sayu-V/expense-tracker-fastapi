\# Expense Tracker API (FastAPI)



A REST API backend for tracking personal expenses, built with \*\*FastAPI\*\*, \*\*Python\*\*, and \*\*Docker\*\*.



This project demonstrates how to design and implement a scalable backend API with proper documentation, version control, and architecture planning.



---



\# Features



\* Expense CRUD operations

\* Category management

\* Expense filtering

\* Budget tracking

\* Expense analytics

\* CSV export

\* REST API design

\* Swagger API documentation



---



\# Tech Stack



| Component         | Technology        |

| ----------------- | ----------------- |

| Language          | Python            |

| API Framework     | FastAPI           |

| Containerization  | Docker            |

| API Documentation | Swagger / OpenAPI |

| Future Database   | PostgreSQL        |

| Future ORM        | SQLModel          |



---



\# Architecture



Client

↓

FastAPI Backend

↓

Python Data Storage (current)

↓

PostgreSQL (future)



---



\# Running the Project



\## Start the application



docker compose up --build



\## Access API documentation



http://localhost:8000/docs



---



\# Project Structure



app/

└── main.py



docs/

├── HLD.md

├── LLD.md

└── tech-stack.md



Dockerfile

docker-compose.yml

requirements.txt



---



\# Future Improvements



\* PostgreSQL database integration

\* SQLModel ORM

\* Authentication (JWT)

\* User accounts

\* Deployment to cloud



See \*\*PROJECT\_ROADMAP.md\*\* for the full plan.



---



\# API Documentation



FastAPI automatically generates API documentation:



Swagger UI



http://localhost:8000/docs



---



\# License



MIT License



