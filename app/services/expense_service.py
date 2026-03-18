from app.storage.memory_db import expenses, budget
from app.storage.memory_db import categories

def get_expenses(page, limit, category=None, min_amount=None, max_amount=None):
    from app.storage.memory_db import expenses

    data = expenses

     # filter by category
    if category:
        data = [e for e in data if e["category"] == category]

     # filter by amount
    if min_amount is not None:
        data = [e for e in data if e["amount"] >= min_amount]

    if max_amount is not None:
        data = [e for e in data if e["amount"] <= max_amount]

    total = len(data)

    # pagination
    start = (page - 1) * limit
    end = start + limit

    return {
        "items": data[start:end],
        "total": total
    }


def get_expense_by_id(expense_id: int):
    for e in expenses:
        if e["id"] == expense_id:
            return e
    return None



def create_expense(expense, expense_id, categories):
    # validate category
    if expense.category not in [c["name"] for c in categories]:
        return None, "Invalid category"

    if not validate_category(expense.category):
    raise ValueError("Invalid category. Please create category first.")

    new_expense = {
        "id": expense_id,
        "category": expense.category,
        "amount": expense.amount,
        "note": expense.note,
    }

    # ✅ THIS WAS MISSING
    expenses.append(new_expense)

    # ✅ update budget
    budget["spent"] += expense.amount

    return new_expense, None


def validate_category(category_name: str):
    for cat in categories:
        if cat["name"].lower() == category_name.lower():
            return True
    return False


def update_expense(expense_id: int, expense, categories):
    data = expense.dict()

    category_obj = next((c for c in categories if c["name"] == data["category"]), None)

    if not category_obj:
        return None, "Invalid category"

    for e in expenses:
        if e["id"] == expense_id:
            e["category"] = data["category"]
            e["amount"] = data["amount"]
            e["note"] = data.get("note", "")
            return e, None

    return None, "Expense not found"


def delete_expense(expense_id):

    for e in expenses:
        if e["id"] == expense_id:
            budget["spent"] -= e["amount"]  # ✅ important
            expenses.remove(e)
            return True

    return False
