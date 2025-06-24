from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from server.app import db  
from server.models.user import User  

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    if not data.get('username') or not data.get('password'):
        return jsonify(message="Username and password are required"), 400

    if User.query.filter_by(username=data['username']).first():
        return jsonify(message="User already exists"), 409

    user = User(username=data['username'])
    user.password_hash = data['password']  
    db.session.add(user)
    db.session.commit()

    return jsonify(message="User created successfully"), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    if not data.get('username') or not data.get('password'):
        return jsonify(message="Username and password are required"), 400

    user = User.query.filter_by(username=data['username']).first()

    if user and user.authenticate(data['password']):
        access_token = create_access_token(identity=user.id)
        return jsonify(access_token=access_token), 200

    return jsonify(message="Invalid username or password"), 401