from collections import defaultdict
from app.storage.memory_db import expenses


def get_top_categories():
    category_totals = defaultdict(float)

    for e in expenses:
        category = e.get("category", "Unknown")
        amount = e.get("amount", 0)
        category_totals[category] += amount

    return dict(sorted(category_totals.items(), key=lambda x: x[1], reverse=True))


def get_expense_trends():
    trends = defaultdict(float)

    for e in expenses:
        date = e.get("date")
        amount = e.get("amount", 0)
        trends[date] += amount

    return dict(sorted(trends.items()))


def get_expense_histogram():
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
