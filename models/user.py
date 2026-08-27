from typing import Optional
from sqlmodel import Field, SQLModel

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    email: str
    password: str
from abc import ABC, abstractmethod
from user_role import Role

class User(ABC):
    def __init__(self, fullName: str, userName: str, password: str, role: Role):
        self.fullName = fullName
        self.userName = userName
        self._password = password
        self.role = role

    @abstractmethod
    def show_profile(self):
        pass
        