from models.admin import Admin, CreateAdmin
from repositories.admin_repository import AdminRepository


class AdminService:

    def __init__(self, repository: AdminRepository):
        self.repository = repository

    def create_first_admin(self, data: CreateAdmin) -> Admin:

        admin = Admin(
            username=data.username,
            email=data.email,
            password=data.password,
        )

        return self.repository.save_admin(admin)