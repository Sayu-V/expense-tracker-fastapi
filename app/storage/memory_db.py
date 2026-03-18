"""
In-Memory Database (Temporary Storage)

This simulates a database.
NOTE:
- Data will reset when server restarts
- Used only for development/testing
"""

# -------------------------------
# CATEGORY STORAGE
# -------------------------------

# Default categories (seed data)
categories = [
    {"id": 1, "name": "Food"},
    {"id": 2, "name": "Transport"},
    {"id": 3, "name": "Shopping"}
]

# Counter for new categories
next_category_id = 4


# -------------------------------
# EXPENSE STORAGE
# -------------------------------

expenses = []

# Counter for expenses
next_expense_id = 1


# -------------------------------
# BUDGET STORAGE
# -------------------------------

budgets = {}
