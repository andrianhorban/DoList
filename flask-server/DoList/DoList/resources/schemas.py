from marshmallow import fields, Schema


class ItemBaseSchema(Schema):
    id = fields.Integer(required=True)
    title = fields.String(required=True)
    text = fields.String(default='')
    slug = fields.String(required=True)
    is_completed = fields.Boolean(default=False)


class ItemResponseSchema(ItemBaseSchema):
    pass
