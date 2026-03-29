from marshmallow import Schema, fields, post_load, post_dump

from backend.entity.user_entity import UserEntity
from backend.schema.__base_schema import BaseSchema
from backend.schema.role_schema.role_reponse import RoleResponseSchema
from backend.client.file_service_client import FileServiceClient

class UserResponseSchema(BaseSchema):
    username = fields.Str()
    password = fields.Str()
    email = fields.Str()
    phone = fields.Str()
    address = fields.Str()
    is_active = fields.Boolean()
    file = fields.Raw(dump_only=True)
    image_url = fields.Str()
    role = fields.Nested(RoleResponseSchema)
    
    @post_load
    def to_user_entity(self, data, **kwargs):
        try:
            return data
        except TypeError as e:
            raise ValueError(f"Invalid data: {e}")

    @post_dump
    def include_file(self, data, **kwargs):
        print("đã vào đây")
        print(data['image_url'])
        if 'image_url' in data and data['image_url'] is not None:
            file_data = FileServiceClient().get_file_by_id(data['image_url'])
            data['file'] = file_data
            del data['image_url']
        
        return data