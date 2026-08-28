from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime
import uuid

class Comment(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    content: str
    author_id: str = Field(foreign_key="user.id")
    post_id: str = Field(foreign_key="post.id")
    created_at: datetime = Field(default_factory=datetime.now)
