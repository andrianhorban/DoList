"""App api"""
from flask_restful import Resource, marshal_with
from DoList import db
from .serializers import ItemListSchema
from ..models import Item


class ItemsResource(Resource):
    @marshal_with(ItemListSchema)
    def get(self):
        """get"""
        try:

            return Item.query.all()
        except Exception:
            return {'message': "Getting exception."}, 500

    #@marshal_with(ItemListSchema)
    def delete(self, item_id: int):
        """del"""
        try:
            item = Item.query.filter(Item.id == item_id).one()
            item.delete()
            return {'message': "Item deleted."}, 204
        except Exception:
            return {'message': "Deleting exception."}, 500

