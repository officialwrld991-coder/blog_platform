from user import User
from user_role import Role

class Admin(User):
    def __init__(self, fullName: str, userName: str, password: str):
        super().__init__(fullName, userName, password, Role.ADMIN)

    def showProfile(self):
        return f"{self.userName}"
    