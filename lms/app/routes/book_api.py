from flask import Blueprint, jsonify, request
from app import DAO
from Controllers import UserManager, BookManager

book_api = Blueprint('book_api', __name__)

book_manager = BookManager(DAO)
user_manager = UserManager(DAO)

@book_api.route('/api/books/', defaults={'id': None})
@book_api.route('/api/books/<id>')
def get_books(id):
    if id is not None:
        book = book_manager.getBook(id)
        return jsonify(book)
    else:
        books = book_manager.list()
        return jsonify(books)

@book_api.route('/api/books/reserve/<id>', methods=['POST'])
def reserve_book(id):
    user_id = request.json.get('user_id')
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400
    
    result = book_manager.reserve(user_id, id)
    return jsonify({"message": "Book reserved", "result": result})

@book_api.route('/api/books/search')
def search_books():
    keyword = request.args.get('keyword')
    if not keyword:
        return jsonify({"error": "Keyword is required"}), 400
    
    results = book_manager.search(keyword)
    return jsonify({"books": results, "count": len(results), "keyword": keyword})

@book_api.route('/api/user/reserved_books')
def get_reserved_books():
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({"error": "User ID is required"}), 400
    
    reserved_books = book_manager.getReserverdBooksByUser(user_id=user_id)
    if reserved_books is None:
        return jsonify({"error": "No reserved books found"}), 404
    
    user_books = reserved_books['user_books'].split(',')
    return jsonify({"reserved_books": user_books})