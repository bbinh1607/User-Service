from backend.schema.__base_schema import BaseSchema
from marshmallow import fields, post_load
from backend.entity.refresh_token_entity import RefreshTokenEntity
from dataclasses import dataclass
from datetime import datetime

@dataclass
class RefreshTokenSchemaDTO:
    user_id: str
    refresh_token: str
    expires_at: datetime

class RefreshTokenSchema(BaseSchema):
    user_id = fields.Str()
    refresh_token = fields.Str()
    expires_at = fields.DateTime()
    
    @post_load
    def validate_refresh_token(self, data, **kwargs):
        try:
            return RefreshTokenEntity(**data)
        except TypeError as e:
            raise ValueError(f"Error converting data to RefreshTokenSchemaDTO: {e}")