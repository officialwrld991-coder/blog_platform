from fastapi import FastAPI
from models.user import User
from database import create_db_and_tables
from contextlib import asynccontextmanager
import models


@asynccontextmanager
async def lifespan(app:FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)
