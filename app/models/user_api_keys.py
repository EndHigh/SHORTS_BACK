from app.models.base import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models.enums import StatusEnum

class UserApiKeys(Base):
    __tablename__ = "user_api_keys"
    
    key_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    api_key = Column(String(255), nullable=False)
    status = Column(Enum(StatusEnum), nullable=False, default=StatusEnum.ACTIVE)
    created_at = Column(DateTime, default=datetime.utcnow)
    last_used_at = Column(DateTime)
    
    # Relationships
    user = relationship("Users", back_populates="api_keys")