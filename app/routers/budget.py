from fastapi import APIRouter
from app.storage.memory_db import budgets, expenses

router = APIRouter(prefix="/budget", tags=["Budget"])

@router.post("")
def set_budget(limit: float):
    budgets["limit"] = limit
    return budgets

@router.get("")
def get_budget():
    return budgets

@router.get("/status")
def budget_status():
    spent = sum(e["amount"] for e in expenses)
    remaining = budgets["limit"] - spent

    return {
        "budget": budgets["limit"],
        "spent": spent,
        "remaining": remaining
    }
