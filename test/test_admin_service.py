import pytest
from sqlmodel import SQLModel, Session, create_engine
from dtos.requests import CreateAdminRequest
from repositories.admin_repository import AdminRepository
from services.admin_service import AdminService
from utils.password import verify_password

engine = create_engine(
    "sqlite://",
    connect_args={"check_same_thread": False},
)


class TestAdminService:

    @pytest.fixture
    def session(self):
        SQLModel.metadata.create_all(engine)

        with Session(engine) as session:
            yield session

        SQLModel.metadata.drop_all(engine)

    def test_create_first_admin(self, session):
        repository = AdminRepository(session)
        service = AdminService(repository)

        data = CreateAdminRequest(
            username="first admin",
            email="adminone@gmail.com",
            password="password",
        )

        created_admin = service.create_first_admin(data)

        assert created_admin.id is not None
        assert created_admin.username == "first admin"
        assert created_admin.email == "adminone@gmail.com"
        assert created_admin.role.value == "Admin"

    def test_cannot_create_second_admin(self, session):
        repository = AdminRepository(session)
        service = AdminService(repository)

        first_admin = CreateAdminRequest(
            username="first admin",
            email="adminone@gmail.com",
            password="password",
        )

        service.create_first_admin(first_admin)

        second_admin = CreateAdminRequest(
            username="second admin",
            email="admintwo@gmail.com",
            password="password",
        )

        with pytest.raises(ValueError, match="An admin already exists"):
            service.create_first_admin(second_admin)