from app.models.base import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum, Text, JSON
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models.enums import StatusEnum

class VideoProjects(Base):
    __tablename__ = "video_projects"
    
    project_id = Column(Integer, primary_key=True, autoincrement=True)
    news_id = Column(Integer, ForeignKey("news_articles.news_id"))
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    status = Column(Enum(StatusEnum), nullable=False, default=StatusEnum.PENDING)
    summary_script = Column(Text)
    final_video_path = Column(String(255))
    final_metadata_json = Column(JSON)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationships
    user = relationship("Users", back_populates="video_projects")
    news_article = relationship("NewsArticles", back_populates="video_projects")
    usage_history = relationship("UserAiUsageHistory", back_populates="project")
    project_keywords = relationship("ProjectKeywords", back_populates="project")
    assets = relationship("Assets", back_populates="project")
    social_uploads = relationship("SocialUploads", back_populates="project")