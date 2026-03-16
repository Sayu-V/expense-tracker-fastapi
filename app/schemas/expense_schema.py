from pydantic import BaseModel
from enum import Enum
from app.storage.memory_db import categories

# Build enum values from category list
class CategoryEnum(str, Enum):
    pass

# Dynamically add categories to Enum
for c in categories:
    setattr(CategoryEnum, c["name"], c["name"])

class Expense(BaseModel):
    category: CategoryEnum
    amount: float
    note: str | None = None
