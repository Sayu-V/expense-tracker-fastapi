from app.storage.memory_db import expenses


def get_expenses(page: int, limit: int):
    start = (page - 1) * limit
    end = start + limit

    paginated_expenses = expenses[start:end]

    return {
        "items": paginated_expenses,
        "total": len(expenses)
    }
