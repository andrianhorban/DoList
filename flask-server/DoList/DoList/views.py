"""DoList views"""
from flask import Blueprint, request
from DoList import db
from .models import Item

blueprint_DoList = Blueprint('DoList', __name__)
