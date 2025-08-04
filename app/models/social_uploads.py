from app.models.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Enum, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models.enums import PlatformEnum, UploadStatusEnum

class SocialUploads(Base):
    __tablename__ = "social_uploads"
    
    upload_id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey("video_projects.project_id"), nullable=False)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    platform = Column(Enum(PlatformEnum), nullable=False)
    post_url = Column(String(2048))
    upload_status = Column(Enum(UploadStatusEnum), nullable=False, default=UploadStatusEnum.UPLOADING)
    uploaded_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    project = relationship("VideoProjects", back_populates="social_uploads")
    user = relationship("Users", back_populates="social_uploads")