from pydantic import BaseModel
from typing import Any, Optional


class Pagination(BaseModel):
    page: int
    limit: int
    total: int


class APIResponse(BaseModel):
    status: str
    data: Any | None = None
    pagination: Optional[Pagination] = None
