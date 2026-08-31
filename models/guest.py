from datetime import datetime, timezone
from uuid import UUID, uuid4
from typing import Optional
from pydantic import BaseModel
from models.user import User
from models.user_role import Role


class createGuest(BaseModel):
    username: str
    email: str
    password: str
    role = Role.GUEST

class updateGuest(BaseModel):
    username: Optional [str] = None
    email: Optional [str] = None
    password: Optional [str] = None

class Guest(User, table=True):
    password: str

class GuestResponse(BaseModel):
    id: UUID
    username: str
    email: str
    created_at: datetime

    class Config:
        from_attributes = True


