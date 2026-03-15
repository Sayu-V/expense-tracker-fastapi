from fastapi import APIRouter
from fastapi.responses import FileResponse
import csv
from app.storage.memory_db import expenses

router = APIRouter(prefix="/export", tags=["Export"])

@router.get("/csv")
def export_csv():
    file = "expenses.csv"

    with open(file, "w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=["id", "category", "amount", "note", "date"]
        )
        writer.writeheader()
        writer.writerows(expenses)

    return FileResponse(file, media_type="text/csv", filename="expenses.csv")
