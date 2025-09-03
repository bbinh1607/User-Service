from marshmallow import Schema, fields, post_load

class RefreshTokenSchema(Schema):
    refresh_token = fields.Str(required=True)

    @post_load
    def make_token(self, data, **kwargs):
        # Trả thẳng giá trị của refresh_token
        return data["refresh_token"]
