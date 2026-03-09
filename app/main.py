from pydantic import BaseModel
from fastapi import FastAPI
from datetime import date
import csv
from fastapi.responses import FileResponse
from datetime import date

class Expense(BaseModel):
    category: str
    amount: float
    note: str = ""
    date: str


class Expense(BaseModel):
    category: str
    amount: float
    note: str = ""
    date: str = str(date.today())


app = FastAPI()

expenses = []
categories = ["Food", "Transport", "Shopping"]
budget = {"limit": 0}

# -----------------------------
# CORE EXPENSE CRUD
# -----------------------------

@app.get("/expenses")
def get_expenses():
    return expenses

@app.get("/expenses/{expense_id}")
def get_expense(expense_id: int):
    for e in expenses:
        if e["id"] == expense_id:
            return e
    return {"error": "Expense not found"}



@app.post("/expenses")
def add_expense(expense: Expense):
    expense_id = len(expenses) + 1
    
    data = expense.dict()   # convert model to dictionary
    data["id"] = expense_id
    
    expenses.append(data)
    
    return data

@app.put("/expenses/{expense_id}")
def update_expense(expense_id: int, category: str, amount: float):
    for e in expenses:
        if e["id"] == expense_id:
            e["category"] = category
            e["amount"] = amount
            return e
    return {"error": "Expense not found"}

@app.delete("/expenses/{expense_id}")
def delete_expense(expense_id: int):
    global expenses
    expenses = [e for e in expenses if e["id"] != expense_id]
    return {"message": "Expense deleted"}

@app.delete("/expenses")
def delete_all():
    expenses.clear()
    return {"message": "All expenses removed"}

# -----------------------------
# CATEGORY MANAGEMENT
# -----------------------------

@app.get("/categories")
def get_categories():
    return categories

@app.post("/categories")
def add_category(name: str):
    categories.append(name)
    return categories

@app.put("/categories/{index}")
def rename_category(index: int, name: str):
    categories[index] = name
    return categories

@app.delete("/categories/{index}")
def delete_category(index: int):
    categories.pop(index)
    return categories

# -----------------------------
# FILTERING
# -----------------------------

@app.get("/expenses/filter/category")
def filter_category(category: str):
    return [e for e in expenses if e["category"] == category]

@app.get("/expenses/filter/date")
def filter_date(expense_date: str):
    return [e for e in expenses if e["date"] == expense_date]

@app.get("/expenses/filter/amount")
def filter_amount(min: float, max: float):
    return [e for e in expenses if min <= e["amount"] <= max]

# -----------------------------
# STATISTICS / REPORTS
# -----------------------------

@app.get("/summary")
def summary():
    total = sum(e["amount"] for e in expenses)
    return {"total_expense": total}

@app.get("/summary/category")
def category_summary():
    result = {}
    for e in expenses:
        result[e["category"]] = result.get(e["category"], 0) + e["amount"]
    return result

# -----------------------------
# BUDGET
# -----------------------------

@app.post("/budget")
def set_budget(limit: float):
    budget["limit"] = limit
    return budget

@app.get("/budget")
def get_budget():
    return budget

@app.get("/budget/status")
def budget_status():
    spent = sum(e["amount"] for e in expenses)
    remaining = budget["limit"] - spent
    return {
        "budget": budget["limit"],
        "spent": spent,
        "remaining": remaining
    }

# -----------------------------
# SEARCH
# -----------------------------

@app.get("/expenses/search")
def search_expenses(q: str):
    return [e for e in expenses if q.lower() in e["note"].lower()]

# -----------------------------
# EXPORT CSV
# -----------------------------

@app.get("/export/csv")
def export_csv():
    file = "expenses.csv"
    with open(file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "category", "amount", "note", "date"])
        writer.writeheader()
        writer.writerows(expenses)

    return FileResponse(file, media_type="text/csv", filename="expenses.csv")

# -----------------------------
# INSIGHTS
# -----------------------------

@app.get("/insights")
def insights():
    if not expenses:
        return {"message": "No data"}

    largest = max(expenses, key=lambda x: x["amount"])
    avg = sum(e["amount"] for e in expenses) / len(expenses)

    category_count = {}
    for e in expenses:
        category_count[e["category"]] = category_count.get(e["category"], 0) + 1

    most_used = max(category_count, key=category_count.get)

    return {
        "largest_expense": largest,
        "average_expense": avg,
        "most_used_category": most_used
    }