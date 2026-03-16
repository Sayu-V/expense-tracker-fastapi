from pydantic import BaseModel
from enum import Enum
from app.storage.memory_db import categories


# Build enum dictionary
category_dict = {c["name"]: c["name"] for c in categories}

# Create Enum dynamically
CategoryEnum = Enum("CategoryEnum", category_dict, type=str)


class Expense(BaseModel):
    category: CategoryEnum
    amount: float
    note: str | None = None
