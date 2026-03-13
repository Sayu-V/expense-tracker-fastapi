from fastapi import APIRouter
from collections import defaultdict
from app.storage.memory_db import expenses

router = APIRouter(prefix="/analytics", tags=["Analytics"])


# Top spending categories
@router.get("/top-categories")
def top_categories():
    category_totals = defaultdict(float)

    for e in expenses:
        category = e.get("category")
        amount = e.get("amount", 0)
        category_totals[category] += amount

    return dict(sorted(category_totals.items(), key=lambda x: x[1], reverse=True))


# Expense trends (spending per date)
@router.get("/expense-trends")
def expense_trends():
    trends = defaultdict(float)

    for e in expenses:
        date = e.get("date")
        amount = e.get("amount", 0)
        trends[date] += amount

    return dict(sorted(trends.items()))


# Histogram of expense amounts
@router.get("/histogram")
def expense_histogram():

    buckets = {
        "0-100": 0,
        "100-500": 0,
        "500-1000": 0,
        "1000+": 0
    }

    for e in expenses:
        amount = e.get("amount", 0)

        if amount <= 100:
            buckets["0-100"] += 1
        elif amount <= 500:
            buckets["100-500"] += 1
        elif amount <= 1000:
            buckets["500-1000"] += 1
        else:
            buckets["1000+"] += 1

    return buckets
