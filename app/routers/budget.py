from app.storage.memory_db import budget
from app.schemas.api_response import APIResponse


@router.post("", response_model=APIResponse)
def set_budget(limit: float):
    budget["limit"] = limit
    budget["spent"] = 0

    return APIResponse(
        status="success",
        data=budget
    )


@router.get("", response_model=APIResponse)
def get_budget():
    return APIResponse(
        status="success",
        data=budget
    )


@router.get("/status", response_model=APIResponse)
def budget_status():
    remaining = budget["limit"] - budget["spent"]

    return APIResponse(
        status="success",
        data={
            "limit": budget["limit"],
            "spent": budget["spent"],
            "remaining": remaining
        }
    )
