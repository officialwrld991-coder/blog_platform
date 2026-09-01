from fastapi import FastAPI
from app.controllers.blogger_controller import router as blogger_router
app = FastAPI()

app.include_router(blogger_router)
