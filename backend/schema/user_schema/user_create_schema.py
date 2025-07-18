from marshmallow import Schema, fields, post_load

from backend.entity.user_entity import UserEntity

class UserCreateSchema(Schema):
    username = fields.Str(required=True )
    password = fields.Str(required=True )
    email = fields.Str()
    phone = fields.Str()
    address = fields.Str()
    role_id = fields.Str()
    
    @post_load
    def to_user_entity(self, data, **kwargs):
        try:
            return UserEntity(**data)
        except TypeError as e:
            raise ValueError(f"Invalid data: {e}")

    