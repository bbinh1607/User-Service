from datetime import datetime
from backend.extensions import db
from sqlalchemy import Column, String, DateTime
import uuid

class BaseEntity(db.Model):
    __abstract__ = True

    def _generate_uuid(self):
        return str(uuid.uuid4())

    id = Column(String, primary_key=True, default=_generate_uuid)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow, onupdate=datetime.utcnow) 