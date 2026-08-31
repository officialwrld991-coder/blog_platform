from fastapi import FastAPI
from database import create_db_and_tables
from contextlib import asynccontextmanager
import models


@asynccontextmanager
async def lifespan(app:FastAPI):
    create_db_and_tables()
    yield

app = FastAPI(lifespan=lifespan)

import uvicorn

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

