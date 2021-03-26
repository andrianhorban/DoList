"""App api"""
from flask_restful import Resource, marshal_with, reqparse
from DoList import db
from .serializers import ItemListSchema
from ..models import Item
from flask import request, jsonify


class ItemsResource(Resource):
    @marshal_with(ItemListSchema)
    def get(self):
        """get"""
        try:
            return Item.query.all()
        except Exception:
            return {'message': "Getting exception."}, 500

    @marshal_with(ItemListSchema)
    def delete(self, item_id: int):
        """del"""
        try:
            item = Item.query.filter(Item.id == item_id).one()
            item.delete()
            return {'message': "Item deleted."}, 204
        except Exception:
            return {'message': "Deleting exception."}, 500

    # @marshal_with(ItemListSchema)
    def post(self, *args):
        """post"""
        parser = reqparse.RequestParser()
        parser.add_argument('title')
        parser.add_argument('text')
        parser.add_argument('is_completed')
        parser = parser.parse_args()
        title = parser['title']
        text = parser['text']
        is_completed = bool(parser['is_completed'])
        response = {
            'title': title,
            'text': text,
            'is_completed': is_completed
        }
        return jsonify(response)

    @marshal_with(ItemListSchema)
    def put(self, item_id):
        """put"""
        try:
            item = Item.query.filter(Item.id == int(item_id)).first()
            item.title = request.form['title']
            item.text = request.form['text']
            item.slug = request.form['slug']
            item.is_completed = request.form['is_completed']
            db.session.commit()
            db.session.close()
            return Item.query.all()
        except Exception:
            return {'message': "Put exception."}, 500
