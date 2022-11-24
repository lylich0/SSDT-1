from marshmallow import Schema, fields


class UserSchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)


class CategorySchema(Schema):
    id = fields.Str(dump_only=True)
    name = fields.Str(required=True)


class RecordSchema(Schema):
    id = fields.Str(dump_only=True)
    user_id = fields.Str(required=True)
    category_id = fields.Str(required=True)
    date = fields.Str(dump_only=True)
    amount = fields.Str(required=True)
