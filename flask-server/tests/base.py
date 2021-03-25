"""Base class for testing"""
from unittest import TestCase
from DoList import db
from app import app
from DoList.DoList.models import Item


class BaseTestCase(TestCase):
    """A base test case."""
    def create_app(self):
        app.config.from_object('config.TestConfig')
        return app

    def setUp(self):
        db.create_all()
        db.session.add(Item(1, "title slug", "some random text", "title-slug", True))

        db.session.commit()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
