import pytest
import asyncio
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.db_session import get_db_session
from app.models.templates import Templates

@pytest.mark.asyncio
async def test_insert_template_async():
    async with get_db_session() as session:  # 커스텀 세션 함수
        dummy = Templates(
            template_name="Async Template",
            settings={"lang": "ko"}
        )

        session.add(dummy)
        await session.commit()
        await session.refresh(dummy)

        assert dummy.template_id is not None
        print(f"Inserted (async) Template ID: {dummy.template_id}")
