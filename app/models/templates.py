from app.models.base import Base
from sqlalchemy import Column, Integer, String, JSON

class Templates(Base):
    __tablename__ = "templates"
    
    template_id = Column(Integer, primary_key=True, autoincrement=True)
    template_name = Column(String(100), nullable=False)
    settings = Column(JSON)