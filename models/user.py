from typing import Optional
from sqlmodel import Field, SQLModel
from datetime import datetime
import uuid

class User(SQLModel, table=True):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()), primary_key=True)
    fullName: str
    userName: str = Field(index=True, unique=True)
    password: str
    role: str = Field(default="GUEST")
    