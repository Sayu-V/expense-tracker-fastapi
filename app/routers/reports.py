from fastapi import APIRouter
from app.data.store import expenses

router = APIRouter(tags=["Reports"])

@router.get("/summary")
def summary():
    total = sum(e["amount"] for e in expenses)
    return {"total_expense": total}

@router.get("/summary/category")
def category_summary():
    result = {}
    for e in expenses:
        result[e["category"]] = result.get(e["category"], 0) + e["amount"]
    return result

@router.get("/insights")
def insights():
    if not expenses:
        return {"message": "No data"}

    largest = max(expenses, key=lambda x: x["amount"])
    avg = sum(e["amount"] for e in expenses) / len(expenses)

    category_count = {}
    for e in expenses:
        category_count[e["category"]] = category_count.get(e["category"], 0) + 1

    most_used = max(category_count, key=category_count.get)

    return {
        "largest_expense": largest,
        "average_expense": avg,
        "most_used_category": most_used
    }
