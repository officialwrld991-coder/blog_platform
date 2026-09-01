from fastapi import FastAPI
from database import create_db_and_tables
from contextlib import asynccontextmanager
from controllers.admin_controller import router as admin_router
from models.admin import Admin
from models.blogger import Blogger
from models.guest import Guest
from models.post import Post
from models.comment import Comment



@asynccontextmanager
async def lifespan(app:FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

app.include_router(admin_router)