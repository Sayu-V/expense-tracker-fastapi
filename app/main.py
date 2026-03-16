from fastapi import FastAPI
from app.routers import expenses, categories, reports, budget, export, analytics
from app.core.exceptions import (
    AppException,
    app_exception_handler,
    generic_exception_handler
)

app = FastAPI()

# routers
app.include_router(expenses.router)
app.include_router(categories.router)
app.include_router(budget.router)
app.include_router(reports.router)
app.include_router(export.router)
app.include_router(analytics.router)

# routers
app.add_exception_handler(AppException, app_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)
