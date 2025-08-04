from app.models.base import Base
from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.orm import relationship
from datetime import datetime

class NewsArticles(Base):
    __tablename__ = "news_articles"
    
    news_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(255), nullable=False)
    content = Column(Text, nullable=False)
    original_url = Column(String(255))
    source = Column(String(50))
    category = Column(String(50))
    published_at = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    video_projects = relationship("VideoProjects", back_populates="news_article")