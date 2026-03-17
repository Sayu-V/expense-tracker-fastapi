from fastapi import APIRouter, Depends
from app.core.dependencies import get_analytics_service
from app.schemas.api_response import APIResponse

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/top-categories", response_model=APIResponse)
def top_categories(service = Depends(get_analytics_service)):
    data = service.get_top_categories()

    return APIResponse(
        status="success",
        data=data
    )


@router.get("/expense-trends")
def expense_trends(service = Depends(get_analytics_service)):
    return service.get_expense_trends()


@router.get("/histogram", response_model=APIResponse)
def expense_histogram(service = Depends(get_analytics_service)):
    data = service.get_expense_histogram()

    return APIResponse(
        status="success",
        data=data
    )


