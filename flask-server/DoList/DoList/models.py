"""model for bd"""
from slugify import slugify
from sqlalchemy import event
from DoList import db
from sqlalchemy.orm import validates


class Item(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    title = db.Column(db.Text, unique=True, nullable=False)
    text = db.Column(db.Text, default='')
    slug = db.Column(db.String(128), unique=True, nullable=False)
    is_completed = db.Column(db.Boolean, default=False, nullable=False)

    def __init__(self,title: str, text: str, slug: str, is_completed: bool):
        self.text = text
        self.title = title
        self.slug = slug
        self.is_completed = is_completed
        print("Item created")

    @validates('title')
    def validate_title(self, key, value):
        if Item.query.filter(Item.title == value).first():
            raise AssertionError('Item with this title already exist')
        return value

    def get_item(self):
        return {
            'id' : self.id,
            'title': self.title,
            'text': self.text,
            'slug': self.slug,
            'is_completed': self.is_completed
        }

    def __repr__(self):
        return f"{Item.title, Item.text, Item.is_completed}"


    def save_db(self):
        db.session.add(self)
        db.session.commit()


