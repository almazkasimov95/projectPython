from pydantic import BaseModel
from typing import List, Optional

class LoginResponse(BaseModel):
    token: str

class ErrorResponse(BaseModel):
    error: str

class UserData(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str  # ОШИБКА! На самом деле — last_name
    avatar: Optional[str] = None

class UserListResponse(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: List[UserData]
    support: dict
