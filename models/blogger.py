
from datetime import datetime, timezone
from uuid import UUID, uuid4
from typing import Optional
from pydantic import BaseModel
from sqlmodel import SQLModel, Field
from models.user_role import Role
class Blogger(SQLModel, table = True):
    id:UUID = Field(default_factory = uuid4, primary_key = True)
    username : str
    email: str
    password : str
    role: Role = Field(default=Role.BLOGGER)
    created_at: datetime = Field(
        default_factory=lambda:datetime.now(timezone.utc)
    )
class CreateBlogger(BaseModel):
    username: str
    email: str
    password: str
    role = Role.BLOGGER
class UpdateBlogger(BaseModel):
    username: Optional [str] = None
    email: Optional [str] = None
    password: Optional [str] = None
class BloggerResponse(BaseModel):
    id: UUID
    username: str
    email: str
    created_at: datetime

    class Config:
        from_attributes = True

