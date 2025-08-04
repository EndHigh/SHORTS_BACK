from app.models.base import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from app.models.enums import AgreementTypeEnum

class UserAgreements(Base):
    __tablename__ = "user_agreements"
    
    agreement_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id"), nullable=False)
    agreement_type = Column(Enum(AgreementTypeEnum), nullable=False)
    agreed_at = Column(DateTime, default=datetime.utcnow)
    agreement_version = Column(String(20))
    
    # Relationships
    user = relationship("Users", back_populates="user_agreements")