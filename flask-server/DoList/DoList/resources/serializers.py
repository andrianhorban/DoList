"""serializer"""
from flask_restful import fields

ItemList = {
    'id': fields.Integer,
    'title': fields.String,
    'text': fields.String,
    'slug': fields.String,
    'is_completed': fields.Boolean
}
