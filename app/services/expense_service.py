"""
Expense Service
Handles all business logic for expenses
"""

from fastapi import HTTPException
from typing import Optional

# Import in-memory DB
from app.storage.memory_db import expenses, budget, categories, next_expense_id


# -------------------------------
# HELPER FUNCTIONS
# -------------------------------

def category_exists(category_name: str) -> bool:
    """Check if category exists in dynamic category list"""
    return any(cat["name"].lower() == category_name.lower() for cat in categories)


def get_category_name(category_name: str) -> str:
    """Return properly formatted category name"""
    for cat in categories:
        if cat["name"].lower() == category_name.lower():
            return cat["name"]
    return None


# -------------------------------
# ADD EXPENSE
# -------------------------------

def add_expense(expense):
    global next_expense_id

    # Validate category
    if not category_exists(expense.category):
        raise HTTPException(status_code=400, detail="Invalid category")

    # Normalize category name
    category_name = get_category_name(expense.category)

    new_expense = {
        "id": next_expense_id,
        "category": category_name,
        "amount": expense.amount,
        "note": expense.note,
        "expense_date": expense.expense_date
    }

    expenses.append(new_expense)
    next_expense_id += 1

    return new_expense


# -------------------------------
# GET ALL EXPENSES (WITH FILTERS)
# -------------------------------

def list_expenses(page: int = 1, limit: int = 10,
                  category: Optional[str] = None,
                  min_amount: Optional[float] = None,
                  max_amount: Optional[float] = None):

    filtered = expenses

    if category:
        filtered = [e for e in filtered if e["category"].lower() == category.lower()]

    if min_amount is not None:
        filtered = [e for e in filtered if e["amount"] >= min_amount]

    if max_amount is not None:
        filtered = [e for e in filtered if e["amount"] <= max_amount]

    # Pagination
    start = (page - 1) * limit
    end = start + limit

    return {
        "data": filtered[start:end],
        "pagination": {
            "page": page,
            "limit": limit,
            "total": len(filtered)
        }
    }


# -------------------------------
# GET SINGLE EXPENSE
# -------------------------------

def get_expense(expense_id: int):
    for e in expenses:
        if e["id"] == expense_id:
            return e

    raise HTTPException(status_code=404, detail="Expense not found")


# -------------------------------
# UPDATE EXPENSE
# -------------------------------

def update_expense(expense_id: int, updated_expense):
    for e in expenses:
        if e["id"] == expense_id:

            if not category_exists(updated_expense.category):
                raise HTTPException(status_code=400, detail="Invalid category")

            e["category"] = get_category_name(updated_expense.category)
            e["amount"] = updated_expense.amount
            e["note"] = updated_expense.note
            e["expense_date"] = updated_expense.expense_date

            return e

    raise HTTPException(status_code=404, detail="Expense not found")


# -------------------------------
# DELETE EXPENSE
# -------------------------------

def delete_expense(expense_id: int):
    for i, e in enumerate(expenses):
        if e["id"] == expense_id:
            return expenses.pop(i)

    raise HTTPException(status_code=404, detail="Expense not found")


# -------------------------------
# DELETE ALL
# -------------------------------

def delete_all_expenses():
    expenses.clear()
    return {"message": "All expenses deleted"}
