from flask_apispec import marshal_with, MethodResource

from .serializers import DoList
from ..models import Item as i
from DoList import db


class ItemsList(MethodResource):
    @marshal_with(DoList)
    def get(self):
        try:
            return i.query.all()
        except Exception:
            return {'message': "Getting exception."}, 500

    @marshal_with(DoList)
    def delete(self, item_id: int):
        try:
            item = i.query.filter(i.id == item_id).one()
            item.delete()
            return {'message': "Item deleted."}, 204
        except Exception:
            return {'message': "Getting exception."}, 500
