from typing import Optional
from fastapi import APIRouter, HTTPException, Query
from app.schemas.expense_schema import Expense
from app.storage.memory_db import expenses, categories, next_expense_id
from app.schemas.api_response import APIResponse, Pagination
from app.services.expense_service import get_expenses
from app.services import expense_service

router = APIRouter(prefix="/expenses", tags=["Expenses"])


# ✅ LIST
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


# ✅ GET BY ID
@router.get("/{expense_id}", response_model=APIResponse)
def get_expense(expense_id: int):
    for e in expenses:
        if e["id"] == expense_id:
            return APIResponse(status="success", data=e)

    raise HTTPException(status_code=404, detail="Expense not found")


# ✅ CREATE
@router.post("", response_model=APIResponse)
def add_expense(expense: Expense):
    global next_expense_id

    data, error = expense_service.create_expense(expense, next_expense_id, categories)

    if error:
        raise HTTPException(status_code=400, detail=error)

    next_expense_id += 1

    return APIResponse(status="success", data=data)


# ✅ UPDATE
@router.put("/{expense_id}", response_model=APIResponse)
def update_expense(expense_id: int, expense: Expense):

    data, error = expense_service.update_expense(expense_id, expense, categories)

    if error == "Invalid category":
        raise HTTPException(status_code=400, detail=error)

    if error == "Expense not found":
        raise HTTPException(status_code=404, detail=error)

    return APIResponse(status="success", data=data)


# ✅ DELETE ONE
@router.delete("/{expense_id}", response_model=APIResponse)
def delete_expense(expense_id: int):

    success = expense_service.delete_expense(expense_id)

    if not success:
        raise HTTPException(status_code=404, detail="Expense not found")

    return APIResponse(
        status="success",
        data={"message": "Expense deleted"}
    )


# ✅ DELETE ALL
@router.delete("", response_model=APIResponse)
def delete_all():
    expenses.clear()

    return APIResponse(
        status="success",
        data={"message": "All expenses removed"}
    )


# ✅ FILTER CATEGORY
@router.get("/filter/category", response_model=APIResponse)
def filter_category(category: str):
    data = [e for e in expenses if e["category"] == category]

    return APIResponse(status="success", data=data)


# ✅ FILTER DATE (FIXED)
@router.get("/filter/date", response_model=APIResponse)
def filter_date(expense_date: str):
    data = [e for e in expenses if e.get("date") == expense_date]

    return APIResponse(status="success", data=data)


# ✅ FILTER AMOUNT (FIXED)
@router.get("/filter/amount", response_model=APIResponse)
def filter_amount(min: float, max: float):
    data = [e for e in expenses if min <= e["amount"] <= max]

    return APIResponse(status="success", data=data)


# ✅ SEARCH (FIXED)
@router.get("/search", response_model=APIResponse)
def search_expenses(
    category: Optional[str] = None,
    note: Optional[str] = None
):
    results = expenses

    if category:
        results = [e for e in results if e["category"].lower() == category.lower()]

    if note:
        results = [e for e in results if note.lower() in e.get("note", "").lower()]

    return APIResponse(status="success", data=results)
