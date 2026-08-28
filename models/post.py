from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime
import uuid

class Post(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    title: str
    content: str
    author_id: str = Field(foreign_key="user.id")
    is_published: bool = Field(default=False)
    created_at: datetime = Field(default_factory=datetime.now)
