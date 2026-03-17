from app.storage.memory_db import expenses, budget


def get_expenses(page, limit, category=None, min_amount=None, max_amount=None):
    data = expenses

    # filter by category
    if category:
        data = [e for e in data if e["category"].lower() == category.lower()]

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


def create_expense(expense, next_id, categories):
    data = expense.dict()
    data["category"] = data["category"].value

    category_obj = next((c for c in categories if c["name"] == data["category"]), None)

    if not category_obj:
        return None, "Invalid category"

    data["id"] = next_id
    expenses.append(data)

    return data, None


def create_expense(expense, next_id, categories):
    data = expense.dict()
    data["category"] = data["category"].value

    # validate category
    category = next((c for c in categories if c["name"] == data["category"]), None)
    if not category:
        return None, "Invalid category"

    data["id"] = next_id
    expenses.append(data)

    # ✅ UPDATE BUDGET HERE
    budget["spent"] += data["amount"]

    return data, None
    


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
