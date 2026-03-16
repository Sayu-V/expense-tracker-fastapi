"""
from pydantic import BaseModel
from datetime import date

class Expense(BaseModel):
    category: str
    amount: float
    note: str = ""
    date: str = str(date.today())
-------
from pydantic import BaseModel
from app.storage.memory_db import categories

# 👇 THIS LINE CREATES DROPDOWN VALUES
category_names = [c["name"] for c in categories]

class Expense(BaseModel):
    category: str
    amount: float
    note: str | None = None
"""

from pydantic import BaseModel
from enum import Enum
from app.storage.memory_db import categories


# 🔹 Dynamically create Enum from category list
CategoryEnum = Enum(
    "CategoryEnum",
    {c["name"]: c["name"] for c in categories}
)

class Expense(BaseModel):
    category: CategoryEnum
    amount: float
    note: str | None = None
