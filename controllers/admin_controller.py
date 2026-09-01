from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import get_session
from dtos.requests import CreateAdminRequest
from dtos.responses import CreateAdminResponse
from repositories.admin_repository import AdminRepository
from services.admin_service import AdminService


router = APIRouter(
    prefix="/admins",
    tags=["Admin"],
)


@router.post(
    "/first",
    response_model=CreateAdminResponse,
)
def create_first_admin(
    data: CreateAdminRequest,
    session: Session = Depends(get_session),
):
    repository = AdminRepository(session)
    service = AdminService(repository)

    return service.create_first_admin(data)

@router.post(
    "/create",
    response_model=CreateAdminResponse,
)
def create_admin(
    data: CreateAdminRequest,
    admin_username: str,
    admin_password: str,
    session: Session = Depends(get_session),
):
    repository = AdminRepository(session)
    service = AdminService(repository)

    return service.create_admin(
        data=data,
        admin_username=admin_username,
        admin_password=admin_password,
    )