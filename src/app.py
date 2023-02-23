from typing import Optional
from fastapi import FastAPI, Depends
from pydantic import BaseModel
from src.routes.users import router as UserRouter

app = FastAPI()

app.include_router(UserRouter, tags=["User"], prefix="/user")


@app.get('/', tags=["Root"])
def read_root():
    return "FASTAPI MONGODB"
