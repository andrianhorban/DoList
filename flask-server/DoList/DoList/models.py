from slugify import slugify
from sqlalchemy import event
from DoList import db
from sqlalchemy.orm import validates


class Item(db.Model):
    id = db.Column(db.INTEGER, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    text = db.Column(db.Text, default='')
    slug = db.Column(db.String(128), unique=True, nullable=False)
    is_completed = db.Column(db.Boolean, default=False, nullable=False)

    @staticmethod
    def slug_generator(target, value: str):
        target.slug = slugify(value)


db.event.listen(Item.title, 'set', Item.slug_generator, retval=False)
