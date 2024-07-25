from flask import Blueprint, request, jsonify, current_app
from app import DAO
from Controllers import UserManager

user_api = Blueprint('user_api', __name__)
user_manager = UserManager(DAO)

@user_api.route('/api/signout', methods=['POST'])
def signout():
    user_manager.signout()
    return jsonify({"message": "Signout successful"})

@user_api.route('/api/user', methods=['GET'])
def get_user():
    user_id = user_manager.user.uid()
    user = user_manager.get(user_id)
    books = user_manager.getBooksList(user_id)
    return jsonify({"user": user, "books": books})

@user_api.route('/api/user/<id>', methods=['GET'])
def get_user_by_id(id):
    current_app.logger.info(id)
    user = user_manager.get(id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"user": user, "books": []})

@user_api.route('/api/user', methods=['PUT'])
def update_user():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    password = data.get('password')
    bio = data.get('bio')

    if not name or not email or not password or not bio:
        return jsonify({"error": "All fields are required"}), 400

    user_id = user_manager.user.uid()
    user_manager.update(name, email, hash(password), bio, user_id)
    return jsonify({"message": "Your info has been updated"})