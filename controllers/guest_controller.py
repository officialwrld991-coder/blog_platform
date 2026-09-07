from uuid import UUID

from fastapi import APIRouter, Depends
from sqlmodel import Session
from database import get_session
from dtos.requests import CreateGuestRequest, UpdateGuestRequest
from dtos.responses import CreateGuestResponse
from repositories.guest_repository import GuestRepository
from services.guest_service import GuestService

router = APIRouter (prefix="/guest", tags=["guest"])

@router.post("/guest", response_model=CreateGuestResponse)
def create_guest(data: CreateGuestRequest, session: Session = Depends(get_session)):
    repository = GuestRepository(session)
    service = GuestService(repository)
    result = service.create_guest(data)
    return  result

@router.get("/{guest_id}", response_model=CreateGuestResponse)
def get_guest(guest_id: UUID, session: Session = Depends(get_session)):
    repository = GuestRepository(session)
    service = GuestService(repository)
    result = service.get_guest(guest_id)
    return result

@router.get("", response_model=list[CreateGuestResponse])
def get_all_guests(session: Session = Depends(get_session)):
    repository = GuestRepository(session)
    service = GuestService(repository)
    result = service.get_all_guests()
    return result

@router.put("/{guest_id}", response_model=CreateGuestResponse)
def update_guest(guest_id: UUID, data: UpdateGuestRequest, session: Session = Depends(get_session)):
    repository = GuestRepository(session)
    service = GuestService(repository)
    result = service.update_guest(guest_id, data)
    return result

@router.delete("/{guest_id}")
def delete_guest(guest_id: UUID, session: Session = Depends(get_session)):
    repository = GuestRepository(session)
    service = GuestService(repository)
    result = service.delete_guest(guest_id)
    return result
