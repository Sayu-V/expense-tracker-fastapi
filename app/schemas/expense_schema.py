from pydantic import BaseModel
from datetime import date

class Expense(BaseModel):
    category: str
    amount: float
    note: str = ""
    date: str = str(date.today())
