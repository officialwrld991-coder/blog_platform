from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session

from app.database import get_session
from app.models.blogger import CreateBlogger, UpdateBlogger
from app.services.blogger_service import BloggerService

router = APIRouter()


@router.post("/bloggers", status_code=201)
def create_blogger(
    blogger: CreateBlogger,
    session: Session = Depends(get_session)
):
    service = BloggerService(session)
    saved_blogger = service.create_blogger(blogger)
    return {
        "username": saved_blogger.username,
        "email": saved_blogger.email
    }
@router.get("/bloggers/{blogger_id}")
def get_blogger(
    blogger_id: UUID,
    session: Session = Depends(get_session)
):
    service = BloggerService(session)
    blogger = service.find_blogger_by_id(blogger_id)

    if blogger is None:
        raise HTTPException(
            status_code=404,
            detail="Blogger not found"
        )
    return {
        "username": blogger.username,
        "email": blogger.email
    }

@router.get("/bloggers/username/{username}")
def get_blogger_by_username(
    username: str,
    session: Session = Depends(get_session)
):
    service = BloggerService(session)
    blogger = service.find_blogger_by_username(username)

    if blogger is None:
        raise HTTPException(
            status_code=404,
            detail="Blogger not found"
        )

    return {
        "username": blogger.username,
        "email": blogger.email
    }

@router.get("/bloggers/email/{email}")
def get_blogger_by_email(
    email: str,
    session: Session = Depends(get_session)
):
    service = BloggerService(session)
    blogger = service.find_blogger_by_email(email)

    if blogger is None:
        raise HTTPException(status_code=404, detail="Blogger not found")

    return {
        "username": blogger.username,
        "email": blogger.email
    }

@router.get("/bloggers")
def get_all_bloggers(
    session: Session = Depends(get_session)
):
    service = BloggerService(session)
    bloggers = service.find_all_bloggers()
    return [
        {
            "username": blogger.username,
            "email": blogger.email
        }
        for blogger in bloggers
    ]

@router.put("/bloggers/{blogger_id}")
def update_blogger(
    blogger_id: UUID,
    blogger_data: UpdateBlogger,
    session: Session = Depends(get_session)
):
    service = BloggerService(session)
    blogger = service.find_blogger_by_id(blogger_id)

    if blogger is None:
        raise HTTPException(status_code=404, detail="Blogger not found")
    blogger.username = blogger_data.username
    blogger.email = blogger_data.email
    blogger.password = blogger_data.password
    updated_blogger = service.update_blogger(blogger)

    return {
        "username": updated_blogger.username,
        "email": updated_blogger.email
    }