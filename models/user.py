
from datetime import datetime, timezone
from uuid import UUID, uuid4
from pydantic import EmailStr
from sqlmodel import SQLModel, Field as SQLField


class User(SQLModel, table=False):
    id: UUID = SQLField(default_factory=uuid4, primary_key=True)
    username: str = SQLField(unique=True, index=True)
    email: EmailStr = SQLField(unique=True, index=True)
    created_at: datetime = SQLField(
        default_factory=lambda: datetime.now(timezone.utc)
    )
