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
    "/first-admin",
    response_model=CreateAdminResponse,
)
def create_first_admin(
    data: CreateAdminRequest,
    session: Session = Depends(get_session),
):
    repository = AdminRepository(session)
    service = AdminService(repository)

    return service.create_first_admin(data)