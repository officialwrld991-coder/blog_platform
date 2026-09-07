import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from dtos.requests import CreateGuestRequest
from services.guest_service import GuestService

import pytest
from sqlmodel import SQLModel, Session, create_engine
from repositories.guest_repository import GuestRepository
from models.guest import Guest

@pytest.fixture
def session():
    engine = create_engine("sqlite:///:memory:")
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

def test_that_i_can_create_guess(session: Session):
    repository = GuestRepository(session)
    service = GuestService(repository)

    data = CreateGuestRequest(username="epson", email="epson@gmail.com", password="epson@3000")
    result = service.create_guest(data)

    assert result is not None
    assert result.username == "epson"
    assert result.email == "epson@gmail.com"
    assert  result.role.value == "Guest"

def test_that_i_can_get_guest(session: Session):
    repository = GuestRepository(session)
    service = GuestService(repository)

    guest = Guest(username="chloe", email="chloe@gmail.com", password="Chloe@3000")
    saved_guest = repository.save_guest(guest)
    result = service.get_guest(saved_guest.id)

    assert result is not None
    assert result.id == saved_guest.id
    assert result.username == "chloe"
    assert result.email == "chloe@gmail.com"
    assert result.role.value == "Guest"

