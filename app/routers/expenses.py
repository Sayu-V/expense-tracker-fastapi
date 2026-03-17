from typing import Optional
from fastapi import APIRouter, HTTPException, Query
from app.schemas.expense_schema import Expense
from app.storage.memory_db import expenses, categories, next_expense_id
from app.schemas.api_response import APIResponse, Pagination
from app.services.expense_service import get_expenses

router = APIRouter(prefix="/expenses", tags=["Expenses"])


# ✅ UPDATED LIST ENDPOINT (only this changed)
@router.get("/", response_model=APIResponse)
def list_expenses(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    category: Optional[str] = None,
    min_amount: Optional[float] = Query(None, ge=0),
    max_amount: Optional[float] = Query(None, ge=0),
):
    if min_amount and max_amount and min_amount > max_amount:
        raise HTTPException(
            status_code=400,
            detail="min_amount cannot be greater than max_amount"
        )

    result = get_expenses(page, limit, category, min_amount, max_amount)

    return APIResponse(
        status="success",
        data=result["items"],
        pagination=Pagination(
            page=page,
            limit=limit,
            total=result["total"]
        )
    )


# ✅ KEEP EVERYTHING BELOW SAME AS OLD

@router.get("/{expense_id}")
def get_expense(expense_id: int):
    for e in expenses:
        if e["id"] == expense_id:
            return e
    raise HTTPException(status_code=404, detail="Expense not found")


@router.post("")
def add_expense(expense: Expense):
    global next_expense_id

    data = expense.dict()
    data["category"] = data["category"].value

    category_obj = next((c for c in categories if c["name"] == data["category"]), None)

    if not category_obj:
        raise HTTPException(status_code=400, detail="Invalid category")

    data["id"] = next_expense_id
    next_expense_id += 1

    expenses.append(data)

    return data


@router.put("/{expense_id}")
def update_expense(expense_id: int, expense: Expense):
    data = expense.dict()

    category_obj = next((c for c in categories if c["name"] == data["category"]), None)

    if not category_obj:
        raise HTTPException(status_code=400, detail="Invalid category")

    for e in expenses:
        if e["id"] == expense_id:
            e["category"] = data["category"]
            e["amount"] = data["amount"]
            e["note"] = data.get("note", "")
            return e

    raise HTTPException(status_code=404, detail="Expense not found")


@router.delete("/{expense_id}")
def delete_expense(expense_id: int):
    for e in expenses:
        if e["id"] == expense_id:
            expenses.remove(e)
            return {"message": "Expense deleted"}

    raise HTTPException(status_code=404, detail="Expense not found")


@router.delete("")
def delete_all():
    expenses.clear()
    return {"message": "All expenses removed"}


@router.get("/filter/category")
def filter_category(category: str):
    return [e for e in expenses if e["category"] == category]


@router.get("/filter/date")
def filter_date(expense_date: str):
    return [e for e in expenses if e.get("date") == expense_date]


@router.get("/filter/amount")
def filter_amount(min: float, max: float):
    return [e for e in expenses if min <= e["amount"] <= max]


@router.get("/search")
def search_expenses(
    category: Optional[str] = None,
    note: Optional[str] = None
):
    results = expenses

    if category:
        results = [e for e in results if e["category"].lower() == category.lower()]

    if note:
        results = [e for e in results if note.lower() in e.get("note", "").lower()]

    return results
