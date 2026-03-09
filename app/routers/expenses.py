from fastapi import APIRouter
from app.schemas.expense_schema import Expense
from app.data.store import expenses

router = APIRouter(prefix="/expenses", tags=["Expenses"])

@router.get("")
def get_expenses():
    return expenses

@router.get("/{expense_id}")
def get_expense(expense_id: int):
    for e in expenses:
        if e["id"] == expense_id:
            return e
    return {"error": "Expense not found"}

@router.post("")
def add_expense(expense: Expense):
    expense_id = len(expenses) + 1
    data = expense.dict()
    data["id"] = expense_id
    expenses.append(data)
    return data

@router.put("/{expense_id}")
def update_expense(expense_id: int, category: str, amount: float):
    for e in expenses:
        if e["id"] == expense_id:
            e["category"] = category
            e["amount"] = amount
            return e
    return {"error": "Expense not found"}

@router.delete("/{expense_id}")
def delete_expense(expense_id: int):
    global expenses
    expenses[:] = [e for e in expenses if e["id"] != expense_id]
    return {"message": "Expense deleted"}

@router.delete("")
def delete_all():
    expenses.clear()
    return {"message": "All expenses removed"}

@router.get("/filter/category")
def filter_category(category: str):
    return [e for e in expenses if e["category"] == category]

@router.get("/filter/date")
def filter_date(expense_date: str):
    return [e for e in expenses if e["date"] == expense_date]

@router.get("/filter/amount")
def filter_amount(min: float, max: float):
    return [e for e in expenses if min <= e["amount"] <= max]

@router.get("/search")
def search_expenses(q: str):
    return [e for e in expenses if q.lower() in e["note"].lower()]
