from fastapi import APIRouter, HTTPException, Query
from app.schemas.api_response import APIResponse
from app.storage.memory_db import budget

router = APIRouter(prefix="/budget", tags=["Budget"])


@router.post("", response_model=APIResponse)
def set_budget(limit: float = Query(..., gt=0)):
    budget["limit"] = limit
    budget["spent"] = 0

    return APIResponse(
        status="success",
        data={"message": "Budget set successfully", "limit": limit}
    )


@router.get("/status", response_model=APIResponse)
def get_budget_status():
    remaining = budget["limit"] - budget["spent"]

    return APIResponse(
        status="success",
        data={
            "limit": budget["limit"],
            "spent": budget["spent"],
            "remaining": remaining
        }
    )
