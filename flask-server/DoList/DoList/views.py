"""DoList views"""
from flask import Blueprint, request, render_template
#from .models import Item
from sqlalchemy import func

blueprint_DoList = Blueprint('DoList', __name__, template_folder='templates')
#
#
# @blueprint_DoList.route('/DoList', methods=('GET',))
# def show_items():
#     q = request.args.get('q')
#     if q:
#         items = Item.query.filter(func.lower(Item.title).contains(q.lower())).all()
#     else:
#         items = Item.query.all()
#     return render_template('DoList/DoList.html', items=items)
