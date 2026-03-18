"""
Expense Schema (Request + Response Models)

IMPORTANT:
- Category is now dynamic (NOT ENUM)
- Validation happens in service layer
"""

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class Expense(BaseModel):
    category: str = Field(..., description="Category name (dynamic)")
    amount: float = Field(..., gt=0, description="Expense amount")
    note: Optional[str] = Field(None, description="Optional note")
    expense_date: Optional[str] = Field(
        default_factory=lambda: datetime.now().strftime("%Y-%m-%d"),
        description="Date of expense"
    )
