from backend.entity._base_entity import BaseEntity
from sqlalchemy import Column, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

class RefreshTokenEntity(BaseEntity):
    __tablename__ = "refresh_token"

    user_id = Column(String, ForeignKey("user.id"), nullable=False, unique=True)
    refresh_token = Column(String, nullable=False, unique=True)
    expires_at = Column(DateTime, nullable=False)

    user = relationship("UserEntity", back_populates="refresh_tokens")
