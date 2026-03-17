from app.storage.memory_db import expenses


def get_expenses(page, limit, category=None, min_amount=None, max_amount=None):

    results = expenses

    if category:
        results = [e for e in results if e["category"] == category]

    if min_amount is not None:
        results = [e for e in results if e["amount"] >= min_amount]

    if max_amount is not None:
        results = [e for e in results if e["amount"] <= max_amount]

    total = len(results)

    start = (page - 1) * limit
    end = start + limit

    return {
        "items": results[start:end],
        "total": total
    }


"""
from app.storage.memory_db import expenses


def get_expenses(page: int, limit: int):
    start = (page - 1) * limit
    end = start + limit

    paginated_expenses = expenses[start:end]

    return {
        "items": paginated_expenses,
        "total": len(expenses)
    }
"""
