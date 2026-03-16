from pydantic import BaseModel
from enum import Enum
from app.storage.memory_db import categories


# build enum
CategoryEnum = Enum(
    "CategoryEnum",
    {c["name"]: c["name"] for c in categories},
    type=str
)


class Expense(BaseModel):
    category: CategoryEnum
    amount: float
    note: str | None = None

    class Config:
        use_enum_values = True
