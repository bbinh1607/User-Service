from marshmallow import fields, post_load, Schema
from backend.entity.user_entity import UserEntity

class AuthLoginSchema(Schema):
    username = fields.Str(required=True)
    password = fields.Str(required=True)


    @post_load
    def validate_login(self, data, **kwargs):
        try:
            return UserEntity(**data)
        except TypeError as e:
            raise ValueError(f"Error converting data to AuthLoginSchema: {e}")