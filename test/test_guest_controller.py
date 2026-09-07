import sys
import os

from dtos.requests import CreateGuestRequest
from controllers.guest_controller import  create_guest
from services.guest_service import GuestService

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
import uuid
from sqlmodel import SQLModel, Session, create_engine
from models.guest import Guest
from repositories.guest_repository import GuestRepository

def test_that_controller_can_create_a_guest():
    data = CreateGuestRequest(username="flynn", email="flynn@gmail.com", password="Linux@3000")
    result = create_guest(data)

    assert result is not None
    assert result.username == "flynn"
    assert result.email == "flynn@gmail.com"
    assert result.role.value == "Guest"
