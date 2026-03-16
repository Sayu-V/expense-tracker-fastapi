from collections import defaultdict
from app.storage.memory_db import expenses, budgets


def get_monthly_summary(month: str):
    total = 0

    for e in expenses:
        if e.get("date", "").startswith(month):
            total += e.get("amount", 0)

    return {
        "month": month,
        "total_expense": total
    }


def get_monthly_category_breakdown(month: str):
    category_totals = defaultdict(float)

    for e in expenses:
        if e.get("date", "").startswith(month):
            category = e.get("category", "Unknown")
            category_totals[category] += e.get("amount", 0)

    return {
        "month": month,
        "categories": dict(category_totals)
    }


def get_budget_vs_expense(month: str):
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
