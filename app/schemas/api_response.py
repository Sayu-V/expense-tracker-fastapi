from pydantic import BaseModel
from typing import Any


class APIResponse(BaseModel):
    status: str
    data: Any | None = None
