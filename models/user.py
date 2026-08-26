from abc import ABC, abstractmethod
from user_role import Role

class User(ABC):
    def __init__(self, fullName, userName, password, role: Role):
        self.fullName = fullName
        self.userName = userName
        self._password = password
        self.role = role