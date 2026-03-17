from typing import Optional
from fastapi import APIRouter, HTTPException, Query
from app.schemas.expense_schema import Expense
from app.storage.memory_db import expenses, categories, next_expense_id
from app.schemas.api_response import APIResponse, Pagination
from app.services.expense_service import get_expenses

router = APIRouter(prefix="/expenses", tags=["Expenses"])


@router.get("", response_model=APIResponse)
def list_expenses(
    page: int = Query(1, ge=1),
    limit: int = Query(10, ge=1, le=100),
    category: Optional[str] = None,
    min_amount: Optional[float] = Query(None, ge=0),
    max_amount: Optional[float] = Query(None, ge=0),
):

    # validation
    if min_amount is not None and max_amount is not None and min_amount > max_amount:
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

