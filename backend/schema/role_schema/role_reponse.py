from marshmallow import fields

from backend.schema.__base_schema import BaseSchema

class RoleResponseSchema(BaseSchema):
    name = fields.Str()
    description = fields.Str()
    rank = fields.Int()
    
    
    