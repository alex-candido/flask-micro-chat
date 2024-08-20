import os
from flask import Blueprint, request, jsonify, abort
from flask_app.modules.__api.v1.users.services.users_services import UserServices

users_controller = Blueprint("ApiUsersController", __name__)
user_services = UserServices()

@users_controller.route("/users", methods=["POST"])
def create_user():
    if request.method != 'POST':
        return
    data = request.get_json()

    if not data:
        return jsonify({"error": "No data provided"}), 400

    email = data.get('email')
    username = data.get('username')
    fullname = data.get('fullname')
    password = data.get('password')

    user_data = {
        "email": email,
        "username": username,
        "fullname": fullname,
        "password": password 
    }

    user = user_services.create_user(user_data)

    return jsonify({
        "data": user.dict()  # Certifique-se de que `user` possui o método `dict()`
    }), 201

@users_controller.route("/users", methods=["GET"])
def get_all_users():
    if request.method == 'GET':
        users = user_services.get_all_users()

        users_list = [user.dict() for user in users]

        return jsonify({
            "data": users_list
        }), 200

@users_controller.route("/users/<uuid:user_id>", methods=["GET"])
def get_user(user_id):
    if request.method == 'GET':
        user = user_services.get_user_by_id(str(user_id))

        if user is None:
            return jsonify({"error": "User not found"}), 404

        user_data = user.dict()
        user_data['id'] = str(user_data['id'])  # Convert UUID to string

        return jsonify({
            "data": user_data
        }), 200

@users_controller.route("/users/<uuid:user_id>", methods=["PUT"])
def update_user(user_id):
    if request.method == 'PUT':
        data = request.get_json()

        if not data:
            return jsonify({"error": "No data provided"}), 400

        user = user_services.update_user(str(user_id), data)
        
        if user is None:
            return jsonify({"error": "User not found"}), 404

        return jsonify({
            "data": user.dict()
        }), 200

@users_controller.route("/users/<uuid:user_id>", methods=["DELETE"])
def delete_user(user_id):
    if request.method == 'DELETE':
        user = user_services.delete_user(str(user_id))
        
        if user is None:
            return jsonify({"error": "User not found"}), 404

        return jsonify({
            "message": "User deleted successfully"
        }), 200
