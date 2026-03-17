from fastapi import APIRouter, Depends
from app.core.dependencies import get_report_service

router = APIRouter(prefix="/reports", tags=["Reports"])


@router.get("/monthly-summary")
def monthly_summary(month: str, service = Depends(get_report_service)):
    return service.get_monthly_summary(month)


@router.get("/monthly-category-breakdown")
def monthly_category_breakdown(month: str, service = Depends(get_report_service)):
    return service.get_monthly_category_breakdown(month)


@router.get("/budget-vs-expense")
def budget_vs_expense(month: str, service = Depends(get_report_service)):
    return service.get_budget_vs_expense(month)

