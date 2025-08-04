# app/api/v1/endpoints/user.py

from fastapi import APIRouter
from typing import List
from app.schemas.user import User

router = APIRouter()

@router.get("/", response_model=List[User])
def read_users():
    return [{"username": "alice"}, {"username": "bob"}]
