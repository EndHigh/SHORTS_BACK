from app.models.base import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.models.enums import AssetTypeEnum

class Assets(Base):
    __tablename__ = "assets"
    
    asset_id = Column(Integer, primary_key=True, autoincrement=True)
    project_id = Column(Integer, ForeignKey("video_projects.project_id"), nullable=False)
    asset_type = Column(Enum(AssetTypeEnum), nullable=False)
    source_info = Column(String(100))
    file_path = Column(String(255))
    license_info = Column(String(100))
    display_order = Column(Integer)
    
    # Relationships
    project = relationship("VideoProjects", back_populates="assets")