from .plugins import db


class Book(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    publication_date = db.Column(db.DateTime)
    author_id = db.Column(db.Integer, db.ForeignKey('author._id'))
    author = db.relationship('Author', backref=db.backref('author'))


class Author(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    dni = db.Column(db.String(10), unique=True)
    birth_date = db.Column(db.DateTime)

    books = db.relationship('Book', backref=db.backref('book'))
