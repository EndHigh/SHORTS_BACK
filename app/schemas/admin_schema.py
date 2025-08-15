from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime
from typing import Optional

class UserBase(BaseModel):
    nickname: str
    role: str
    created_at: Optional[datetime] = None
    user_id: int
    email: EmailStr
    status: str
    updated_at: Optional[datetime] = None

    # class Config:  # Pydantic v1
        # orm_mode = True
    # Pydantic v2에서는 이렇게:
    model_config = ConfigDict(from_attributes=True)

class ReadUser(UserBase):
    pass
