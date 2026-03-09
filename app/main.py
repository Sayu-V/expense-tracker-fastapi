from fastapi import FastAPI

from app.routers import expenses
from app.routers import categories
from app.routers import budget
from app.routers import reports
from app.routers import export

app = FastAPI()

app.include_router(expenses.router)
app.include_router(categories.router)
app.include_router(budget.router)
app.include_router(reports.router)
app.include_router(export.router)
