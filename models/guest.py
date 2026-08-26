from user import User
from user_role import Role

class Guest(User):
    def __init__(self, fullName, userName, password):
        super().__init__(fullName, userName, password, Role.GUEST)
