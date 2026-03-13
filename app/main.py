from fastapi import FastAPI
from app.routers import expenses, categories, reports, budget, export, analytics

app = FastAPI()

app.include_router(analytics.router)
app.include_router(expenses.router)
app.include_router(categories.router)
app.include_router(budget.router)
app.include_router(reports.router)
app.include_router(export.router)
