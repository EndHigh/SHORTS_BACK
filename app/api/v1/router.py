from fastapi import APIRouter
from app.api.v1.endpoints import user
from app.api.v1.endpoints import admin_router

router = APIRouter()

router.include_router(admin_router.router, prefix="/admins", tags=["admins"])
router.include_router(user.router, prefix="/users", tags=["users"])
