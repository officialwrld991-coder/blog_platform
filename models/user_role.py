from abc import ABC, abstractmethod
from enum import Enum

class Role(Enum):
    ADMIN = "Admin"
    GUEST = "Guest"
    USER = "User"
    BLOGGER = "Blogger"