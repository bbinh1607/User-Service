from backend.entity._base_entity import BaseEntity
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship

class RoleEntity(BaseEntity):
    __tablename__ = "role"

    name = Column(String, nullable=False)
    description = Column(String, nullable=False)
    rank = Column(Integer, nullable=False)
    users = relationship("UserEntity", back_populates="role")