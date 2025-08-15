from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.db_session import get_db_session
from app.services.admin.admin_service import read_users
from app.schemas.admin_schema import ReadUser

router = APIRouter()

@router.get("/", response_model=List[ReadUser])
async def get_users(db: AsyncSession = Depends(get_db_session)):
    try:
        user_list = await read_users(db)  # SQLAlchemy 모델 리스트
        return [ReadUser.from_orm(user) for user in user_list]  # ✅ 변환
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"내부 오류 발생: {str(e)}")
