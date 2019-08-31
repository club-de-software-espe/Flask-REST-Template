from flask import Blueprint, Response, request, jsonify
from app.constants import GET, POST, PUT
from .plugins import db
import json
from .models import Author, Book
from .serializers import AuthorSerializer, BookSerializer

urls = Blueprint('urls', __name__)


@urls.route('/author', methods=POST)
def create_author():
    author_serializer = AuthorSerializer()
    new_author = author_serializer.load(request.json, partial=True)
    db.session.add(new_author)
    db.session.commit()
    return Response(json.dumps({'message': 'Author Created'}), status=201)


@urls.route('/author', methods=GET)
def get_authors():
    author_serializer = AuthorSerializer(many=True)
    authors = Author.query.all()
    serialized_authors = author_serializer.dump(authors)
    return jsonify(serialized_authors)


@urls.route('/author/id/<_id>', methods=GET)
def get_author(_id):
    author = Author.query.get(_id)
    author_serializer = AuthorSerializer()
    return author_serializer.jsonify(author)


@urls.route('/author', methods=PUT)
def update_author():
    _id = request.json.get('_id')
    author = Author.query.get(_id)
    if author:
        from datetime import datetime
        author.name = request.json.get('name') or author.name
        author.birth_date = datetime.strptime(request.json.get('birth_date'), '%Y-%m-%d') or author.birth_date
        author.dni = request.json.get('dni') or author.dni
        db.session.commit()
        return Response(json.dumps({'message': 'Author Updated'}), status=201)
    else:
        return Response(json.dumps({'message': 'No matching '}), status=404)


@urls.route('/book', methods=POST)
def create_book():
    book_serializer = BookSerializer()
    new_book = book_serializer.load(request.json, partial=True)
    db.session.add(new_book)
    db.session.commit()
    return Response(json.dumps({'message': 'Book Created'}), status=201)


@urls.route('/book', methods=GET)
def get_books():
    book_serializer = BookSerializer(many=True)
    books = Book.query.all()
    serialized_books = book_serializer.dump(books)
    return jsonify(serialized_books)
