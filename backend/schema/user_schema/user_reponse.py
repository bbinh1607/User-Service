from marshmallow import Schema, fields, post_load

from backend.entity.user_entity import UserEntity
from backend.schema.__base_schema import BaseSchema
from backend.schema.role_schema.role_reponse import RoleResponseSchema

class UserResponseSchema(BaseSchema):
    username = fields.Str()
    password = fields.Str()
    email = fields.Str()
    phone = fields.Str()
    address = fields.Str()
    is_active = fields.Boolean()
    role = fields.Nested(RoleResponseSchema)
    
    @post_load
    def to_user_entity(self, data, **kwargs):
        try:
            return UserEntity(**data)
        except TypeError as e:
            raise ValueError(f"Invalid data: {e}")
