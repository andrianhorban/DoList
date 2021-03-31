"""App api"""
from flask_restful import Resource, reqparse
from DoList import db
from .schemas import ItemResponseSchema, ItemBaseSchema
from .serializers import ItemList
from ..models import Item
from flask import request, jsonify
from flask_apispec import doc, MethodResource, marshal_with


class ItemsResource(MethodResource, Resource):
    @doc(description="Item`s list to do.", tags=['DoList'])
    @marshal_with(ItemBaseSchema(many=True))
    def get(self):
        """get"""
        try:
            return Item.query.all()
        except Exception:
            return {'message': "Getting exception."}, 500


    def delete(self):
        """del
        ---
            paths:
      /api/dolist/{userId}:
        get:
          summary: Returns a user by ID.
          parameters:
            - name: userId
              in: path
              required: true
              description: Parameter description in CommonMark or HTML.
              schema:
                type : integer
                format: int64
                minimum: 1
          responses:
            '200':
              description: OK
        """
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('item_title')
            parser = parser.parse_args()
            item_title = parser['item_title']
            item = Item.query.filter(Item.title == item_title).first()

            db.session.delete(item)
            db.session.commit()
            return {'message': "Item deleted."}, 204
        except Exception:
            return {'message': "Deleting exception."}, 500

    @doc(description="Creating item to do.", tags=['DoList'])
    def post(self, *args):
        """post"""
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('title')
            parser.add_argument('text')
            parser.add_argument('slug')
            parser.add_argument('is_completed')
            parser = parser.parse_args()
            title = parser['title']
            text = parser['text']
            slug = parser['slug']
            is_completed = bool(parser['is_completed'])
            item = Item(title=title, text=text, slug=slug, is_completed=is_completed)
            item.save_db()
            return {'message': "Posted"}, 201
        except Exception:
            return {'message': "Add exception."}, 500

    # @marshal_with(ItemListSchema)
    @doc(description="Editing item to do.", tags=['DoList'])
    @marshal_with(ItemBaseSchema(many=True))
    def put(self):
        """put"""
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('item_title')
            parser.add_argument('title')
            parser.add_argument('text')
            parser.add_argument('slug')
            parser.add_argument('is_completed')
            parser = parser.parse_args()
            item_title = parser['item_title']
            item = Item.query.filter(Item.title == item_title).first()
            item.title = parser['title']
            item.text = parser['text']
            item.slug = parser['slug']
            item.is_completed = bool(parser['is_completed'])

            db.session.commit()
            db.session.close()
            return {'message': "Putted"}, 202
        except Exception:
            return {'message': "Put exception."}, 500
