from fastapi import APIRouter
from collections import defaultdict
from app.storage.memory_db import expenses, budgets

router = APIRouter(prefix="/reports", tags=["Reports"])


# Monthly summary of total expenses
@router.get("/monthly-summary")
def monthly_summary(month: str):
    """
    month format: YYYY-MM
    example: 2026-03
    """

    total = 0

    for e in expenses:
        if e.get("date", "").startswith(month):
            total += e.get("amount", 0)

    return {
        "month": month,
        "total_expense": total
    }


# Category breakdown for a month
@router.get("/monthly-category-breakdown")
def monthly_category_breakdown(month: str):

    category_totals = defaultdict(float)

    for e in expenses:
        if e.get("date", "").startswith(month):
            category = e.get("category")
            category_totals[category] += e.get("amount", 0)

    return {
        "month": month,
        "categories": dict(category_totals)
    }


# Budget vs expense comparison
@router.get("/budget-vs-expense")
def budget_vs_expense(month: str):

    total_expense = 0

    for e in expenses:
        if e.get("date", "").startswith(month):
            total_expense += e.get("amount", 0)

    monthly_budget = budgets.get(month, 0)

    return {
        "month": month,
        "budget": monthly_budget,
        "spent": total_expense,
        "remaining": monthly_budget - total_expense
    }
