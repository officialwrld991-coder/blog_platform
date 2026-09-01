from models.guest import Guest
from models.blogger import Blogger
from models.user_role import Role
from utils.password import hash_password

from repositories.admin_repository import AdminRepository
from repositories.guest_repository import GuestRepository
from repositories.blogger_repository import BloggerRepository


class AuthService:

    def __init__(
        self,
        admin_repository: AdminRepository,
        guest_repository: GuestRepository,
        blogger_repository: BloggerRepository,
    ):
        self.admin_repository = admin_repository
        self.guest_repository = guest_repository
        self.blogger_repository = blogger_repository

    def register(
        self,
        username: str,
        email: str,
        password: str,
        role: Role,
    ):

        if role == Role.ADMIN:
            raise PermissionError(
                "Admin registration is not allowed"
            )

        if role == Role.GUEST:

            if self.guest_repository.find_by_username(username):
                raise ValueError("Username already exists")

            if self.guest_repository.find_by_email(email):
                raise ValueError("Email already exists")

            guest = Guest(
                username=username,
                email=email,
                password=hash_password(password),
            )

            return self.guest_repository.save_guest(guest)

        if role == Role.BLOGGER:

            if self.blogger_repository.find_by_username(username):
                raise ValueError("Username already exists")

            if self.blogger_repository.find_by_email(email):
                raise ValueError("Email already exists")

            blogger = Blogger(
                username=username,
                email=email,
                password=hash_password(password),
            )

            return self.blogger_repository.save_blogger(blogger)

        raise ValueError("Invalid role")