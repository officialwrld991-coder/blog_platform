from datetime import datetime
from uuid import UUID
from typing import Optional
from pydantic import BaseModel
from app.models import User
from app.models.user_role import Role


class createAdmin(BaseModel):
    username: str
    email: str
    password: str
    role = Role.ADMIN

class updateAdmin(BaseModel):
    username: Optional [str] = None
    email: Optional [str] = None
    password: Optional [str] = None

class Admin(User, table=True):
    password: str

class AdminResponse(BaseModel):
    id: UUID
    username: str
    email: str
    created_at: datetime

    class Config:
        from_attributes = True


