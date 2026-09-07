from uuid import UUID

from models.guest import Guest
from dtos.requests import CreateGuestRequest, UpdateGuestRequest, UpdateGuestRequest
from dtos.responses import CreateGuestResponse
from repositories.guest_repository import GuestRepository
from utils.password import hash_password

class GuestService:
    def __init__(self, repository: GuestRepository):
        self.repository = repository

    def create_guest(self, data: CreateGuestRequest):
        existing_user = self.repository.find_by_username(data.username)
        if existing_user:
            raise ValueError("Username already Exists.")

        existing_email = self.repository.find_by_email(data.email)
        if existing_email:
            raise ValueError("Email already Exists.")

        hashed_password = hash_password(data.password)

        guest = Guest(username = data.username, email = data.email, password = hashed_password)
        saved_guest = self.repository.save_guest(guest)
        return  CreateGuestResponse(id=saved_guest.id, username=saved_guest.username, email=saved_guest.email, role=saved_guest.role)

    def get_guest(self, guest_id: UUID):
        guest = self.repository.find_by_id(guest_id)
        if not guest:
            raise ValueError("Guest not found.")
        return  CreateGuestResponse(id=guest.id, email=guest.email, username=guest.username, role=guest.role)

    def get_all_guests(self):
        guests = self.repository.find_all()

        responses = []
        for guest in guests:
            response = CreateGuestResponse(id=guest.id, username=guest.username, email=guest.email, role=guest.role)
            responses.append(response)
        return responses

    def update_guest(self, guest_id: UUID, data: UpdateGuestRequest):
        guest = self.repository.find_by_id(guest_id)

        if not guest:
            raise ValueError("Guest Not Found")
        if data.username is not None:
            guest.username = data.username
        if data.email is not None:
            guest.email = data.email
        if data.password is not None:
            guest.password = hash_password(data.password)

        updated_guest = self.repository.update_guest(guest)
        return CreateGuestResponse(id=updated_guest.id, username=updated_guest.username, email=updated_guest.email, role=updated_guest.role)

    def delete_guest(self, guest_id):
        guest = self.repository.find_by_id(guest_id)

        if not guest:
            raise ValueError("Guest Not Found")
        self.repository.delete_guest(guest)
        return {"message": "Guest Deleted Successfully"}
