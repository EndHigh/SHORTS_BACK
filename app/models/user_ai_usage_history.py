from app.models.base import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric
from sqlalchemy.orm import relationship
from datetime import datetime
from decimal import Decimal

class UserAiUsageHistory(Base):
    __tablename__ = "user_ai_usage_history"
    
    usage_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    project_id = Column(Integer, ForeignKey("video_projects.project_id"))
    ai_service = Column(String(100), nullable=False)
    prompt_tokens = Column(Integer)
    completion_tokens = Column(Integer)
    total_tokens = Column(Integer)
    usage_cost = Column(Numeric(10, 2))
    created_at = Column(DateTime, default=datetime.utcnow)
    
    # Relationships
    user = relationship("Users", back_populates="usage_history")
    project = relationship("VideoProjects", back_populates="usage_history")