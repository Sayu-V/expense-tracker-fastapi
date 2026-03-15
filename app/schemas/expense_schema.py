"""
from pydantic import BaseModel
from datetime import date

class Expense(BaseModel):
    category: str
    amount: float
    note: str = ""
    date: str = str(date.today())
"""

from pydantic import BaseModel
from app.storage.memory_db import categories

# 👇 THIS LINE CREATES DROPDOWN VALUES
category_names = [c["name"] for c in categories]

class ExpenseCreate(BaseModel):
    category: str
    amount: float
    note: str | None = None
