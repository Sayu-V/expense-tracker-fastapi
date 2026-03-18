"""
Expense Service Layer

Responsibilities:
- Business logic
- Validation (category, amounts, etc.)
- Data manipulation (create, update, delete)
"""

from app.storage.memory_db import expenses, budget, categories


# -------------------------------
# CATEGORY VALIDATION
# -------------------------------

def validate_category(category_name: str) -> bool:
    """
    Check if category exists in DB (case-insensitive)
    """
    for cat in categories:
        if cat["name"].lower() == category_name.lower():
            return True
    return False


# -------------------------------
# GET ALL EXPENSES (WITH FILTERS)
# -------------------------------

def get_expenses(page, limit, category=None, min_amount=None, max_amount=None):
    data = expenses

    # filter by category (case-insensitive)
    if category:
        data = [e for e in data if e["category"].lower() == category.lower()]

    # filter by min amount
    if min_amount is not None:
        data = [e for e in data if e["amount"] >= min_amount]

    # filter by max amount
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


# -------------------------------
# GET EXPENSE BY ID
# -------------------------------

def get_expense_by_id(expense_id: int):
    for e in expenses:
        if e["id"] == expense_id:
            return e
    return None


# -------------------------------
# CREATE EXPENSE
# -------------------------------

def create_expense(expense, expense_id):
    """
    Create a new expense
    """

    # ✅ Validate category
    if not validate_category(expense.category):
        return None, "Invalid category. Please create category first."

    # ✅ Create expense object
    new_expense = {
        "id": expense_id,
        "category": expense.category,
        "amount": expense.amount,
        "note": expense.note,
        "expense_date": expense.expense_date
    }

    # ✅ Save expense
    expenses.append(new_expense)

    # ✅ Safe budget update
    if "spent" not in budget:
        budget["spent"] = 0

    budget["spent"] += expense.amount

    return new_expense, None


# -------------------------------
# UPDATE EXPENSE
# -------------------------------

def update_expense(expense_id: int, expense):
    data = expense.dict()

    # ✅ Validate category
    if not validate_category(data["category"]):
        return None, "Invalid category"

    for e in expenses:
        if e["id"] == expense_id:
            e["category"] = data["category"]
            e["amount"] = data["amount"]
            e["note"] = data.get("note", "")
            e["expense_date"] = data.get("expense_date", e.get("expense_date"))
            return e, None

    return None, "Expense not found"


# -------------------------------
# DELETE EXPENSE
# -------------------------------

def delete_expense(expense_id):
    for e in expenses:
        if e["id"] == expense_id:

            # ✅ Safe budget update
            if "spent" in budget:
                budget["spent"] -= e["amount"]

            expenses.remove(e)
            return True

    return False
