from marshmallow import fields


class DoList:
    id = fields.Integer(readOnly=True, description='The unique identifier of item')
    title = fields.String(required=True)
    text = fields.String(description='Items text')
    slug = fields.String(required=True)
    is_completed = fields.Boolean(required=True)
