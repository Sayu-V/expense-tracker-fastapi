from app.storage.memory_db import expenses


def get_expenses(page, limit, category=None, min_amount=None, max_amount=None):
    data = expenses

    # filter by category
    if category:
        data = [e for e in data if e["category"].lower() == category.lower()]

    # filter by amount
    if min_amount is not None:
        data = [e for e in data if e["amount"] >= min_amount]

    if max_amount is not None:
        data = [e for e in data if e["amount"] <= max_amount]

    total = len(data)

    # pagination
    start = (page - 1) * limit
    end = start + limit

    return {
        "items": data[start:end],
        "total": total
    }
