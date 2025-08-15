from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.models import Users

async def read_users(db: AsyncSession):
    stmt = select(Users)
    result = await db.execute(stmt)
    users = result.scalars().all()  # 리스트 반환
    return users
