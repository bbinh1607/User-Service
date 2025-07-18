from backend.entity._base_entity import BaseEntity
from sqlalchemy import Column, String, ForeignKey, Boolean
from sqlalchemy.orm import relationship

class UserEntity(BaseEntity):
    __tablename__ = "user"

    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    email = Column(String)
    phone = Column(String)
    address = Column(String)
    is_active = Column(Boolean, default=True)
    
    role_id = Column(String, ForeignKey("role.id"))
    role = relationship("RoleEntity", back_populates="users")
    refresh_tokens = relationship("RefreshTokenEntity", back_populates="user")