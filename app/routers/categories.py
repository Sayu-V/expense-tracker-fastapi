from fastapi import APIRouter, HTTPException, Depends
from app.storage.memory_db import categories, expenses
from app.core.security import verify_api_key

router = APIRouter(
    prefix="/categories",
    tags=["Categories"],
    dependencies=[Depends(verify_api_key)]
)

@router.get("")
def get_categories():
    return categories


@router.post("")
def add_category(name: str):

    # prevent duplicate categories
    for c in categories:
        if c["name"].lower() == name.lower():
            raise HTTPException(status_code=400, detail="Category already exists")

    new_id = max([c["id"] for c in categories], default=0) + 1

    category = {
        "id": new_id,
        "name": name
    }

    categories.append(category)

    return category


@router.put("/{category_id}")
def rename_category(category_id: int, name: str):

    category = next((c for c in categories if c["id"] == category_id), None)

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    category["name"] = name

    return category


@router.delete("/{category_id}")
def delete_category(category_id: int):

    category = next((c for c in categories if c["id"] == category_id), None)

    if not category:
        raise HTTPException(status_code=404, detail="Category not found")

    # prevent deletion if expenses exist
    for e in expenses:
        if e["category_id"] == category_id:
            raise HTTPException(
                status_code=400,
                detail="Cannot delete category: expenses exist"
            )

    categories.remove(category)

    return {"message": "Category deleted"}
