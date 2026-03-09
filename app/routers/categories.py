from fastapi import APIRouter
from app.data.store import categories

router = APIRouter(prefix="/categories", tags=["Categories"])

@router.get("")
def get_categories():
    return categories

@router.post("")
def add_category(name: str):
    categories.append(name)
    return categories

@router.put("/{index}")
def rename_category(index: int, name: str):
    categories[index] = name
    return categories

@router.delete("/{index}")
def delete_category(index: int):
    categories.pop(index)
    return categories
