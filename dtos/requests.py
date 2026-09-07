from pydantic import BaseModel, EmailStr
from models.user_role import Role
from typing import Optional

class RegisterRequest(BaseModel):
    username: str
    email: EmailStr
    password: str
    role: Role

class LoginRequest(BaseModel):
    username: str
    password: str
    role: Role

class CreateAdminRequest(BaseModel):
    username: str
    email: EmailStr
    password: str

class CreateGuestRequest(BaseModel):
    username: str
    email: EmailStr
    password: str

class UpdateGuestRequest(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None

class UpdateAdminRequest(BaseModel):
    username: Optional [str] = None
    email: Optional [str] = None
    password: Optional [str] = None
