from app.models.base import Base
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

class ProjectKeywords(Base):
    __tablename__ = "project_keywords"
    
    project_id = Column(Integer, ForeignKey("video_projects.project_id"), primary_key=True)
    keyword_id = Column(Integer, ForeignKey("keywords.keyword_id"), primary_key=True)
    
    # Relationships
    project = relationship("VideoProjects", back_populates="project_keywords")
    keyword = relationship("Keywords", back_populates="project_keywords")