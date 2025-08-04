from app.models.base import Base
from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models.enums import RoleEnum, StatusEnum

class Users(Base):
    __tablename__ = "users"
    
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(255), unique=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    nickname = Column(String(100), nullable=False)
    role = Column(Enum(RoleEnum), nullable=False, default=RoleEnum.USER)
    status = Column(Enum(StatusEnum), nullable=False, default=StatusEnum.ACTIVE)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    social_accounts = relationship("SocialAccounts", back_populates="user")
    api_keys = relationship("UserApiKeys", back_populates="user")
    usage_history = relationship("UserAiUsageHistory", back_populates="user")
    video_projects = relationship("VideoProjects", back_populates="user")
    social_uploads = relationship("SocialUploads", back_populates="user")
    user_agreements = relationship("UserAgreements", back_populates="user")