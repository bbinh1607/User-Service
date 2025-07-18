from marshmallow import Schema, fields

class BaseSchema(Schema):
    id = fields.String(required=True)
    created_at = fields.DateTime()
    updated_at = fields.DateTime()