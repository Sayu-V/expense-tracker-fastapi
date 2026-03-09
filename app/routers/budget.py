from fastapi import APIRouter
from app.data.store import budget, expenses

router = APIRouter(prefix="/budget", tags=["Budget"])

@router.post("")
def set_budget(limit: float):
    budget["limit"] = limit
    return budget

@router.get("")
def get_budget():
    return budget

@router.get("/status")
def budget_status():
    spent = sum(e["amount"] for e in expenses)
    remaining = budget["limit"] - spent

    return {
        "budget": budget["limit"],
        "spent": spent,
        "remaining": remaining
    }
