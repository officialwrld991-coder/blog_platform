import pytest
from sqlmodel import SQLModel, Session, create_engine

from dtos.requests import CreateAdminRequest
from dtos.responses import CreateAdminResponse
from models.user_role import Role
from repositories.admin_repository import AdminRepository
from services.admin_service import AdminService


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

    @pytest.fixture
    def service(self, session):
        admin_repository = AdminRepository(session)

        return AdminService(
            admin_repository,
        )

    def test_create_first_admin(self, service):

        data = CreateAdminRequest(
            username="firstadmin",
            email="adminone@gmail.com",
            password="password",
        )

        created_admin = service.create_first_admin(data)

        assert isinstance(created_admin, CreateAdminResponse)
        assert created_admin.id is not None
        assert created_admin.username == "firstadmin"
        assert created_admin.email == "adminone@gmail.com"
        assert created_admin.role == Role.ADMIN

    def test_cannot_create_second_admin(self, service):

        first_admin = CreateAdminRequest(
            username="firstadmin",
            email="adminone@gmail.com",
            password="password",
        )

        service.create_first_admin(first_admin)

        second_admin = CreateAdminRequest(
            username="secondadmin",
            email="admintwo@gmail.com",
            password="password",
        )

        with pytest.raises(
            ValueError,
            match="An admin already exists",
        ):
            service.create_first_admin(second_admin)

    def test_create_another_admin(self, service):

        first_admin = CreateAdminRequest(
            username="firstadmin",
            email="firstadmin@gmail.com",
            password="password123",
        )

        service.create_first_admin(first_admin)

        second_admin = service.create_admin(
            CreateAdminRequest(
                username="secondadmin",
                email="secondadmin@gmail.com",
                password="password456",
            ),
            admin_username="firstadmin",
            admin_password="password123",
        )

        assert isinstance(second_admin, CreateAdminResponse)
        assert second_admin.id is not None
        assert second_admin.username == "secondadmin"
        assert second_admin.email == "secondadmin@gmail.com"
        assert second_admin.role == Role.ADMIN

    def test_create_admin_with_wrong_admin_password(self, service):

        first_admin = CreateAdminRequest(
            username="firstadmin",
            email="firstadmin@gmail.com",
            password="password123",
        )

        service.create_first_admin(first_admin)

        with pytest.raises(
            PermissionError,
            match="Invalid admin credentials",
        ):
            service.create_admin(
                CreateAdminRequest(
                    username="secondadmin",
                    email="secondadmin@gmail.com",
                    password="password456",
                ),
                admin_username="firstadmin",
                admin_password="wrongpassword",
            )

    def test_create_admin_with_nonexistent_admin(self, service):

        first_admin = CreateAdminRequest(
            username="firstadmin",
            email="firstadmin@gmail.com",
            password="password123",
        )

        service.create_first_admin(first_admin)

        with pytest.raises(
            PermissionError,
            match="Invalid admin credentials",
        ):
            service.create_admin(
                CreateAdminRequest(
                    username="secondadmin",
                    email="secondadmin@gmail.com",
                    password="password456",
                ),
                admin_username="doesnotexist",
                admin_password="password123",
            )