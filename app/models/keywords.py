from app.models.base import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

class Keywords(Base):
    __tablename__ = "keywords"
    
    keyword_id = Column(Integer, primary_key=True, autoincrement=True)
    keyword_text = Column(String(100), nullable=False)
    
    # Relationships
    project_keywords = relationship("ProjectKeywords", back_populates="keyword")