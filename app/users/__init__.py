from flask import Blueprint, jsonify, request
from app.users.auth.service import generator_code_phone, verify_code_phone
from app.users.signup.service import create_user
from app.users.login.service import login_user
from app.users.detail.service import get_detail
from app.users.reset.service import reset_password

mod = Blueprint('vm', __name__)


@mod.route("/login", methods=["POST"])
def login():
    email = request.json['email'] if request.json['email'] else ""
    password = request.json['password'] if request.json['password'] else ""
    return jsonify(message=login_user(email, password))


@mod.route("/signup", methods=["POST"])
def signup():
    phone = request.json['phone'] if request.json['phone'] else ""
    password = request.json['password'] if request.json['password'] else ""
    name = request.json['name'] if request.json['name'] else ""
    nickname = request.json['nickname'] if request.json['nickname'] else ""
    email = request.json['email'] if request.json['email'] else ""
    return jsonify(message=create_user(email, nickname, name, password, phone))


@mod.route("/detail", methods=["GET"])
def get_user_detail():
    token = request.headers.get("Authorization")
    return jsonify(message=get_detail(token))


@mod.route("/reset", methods=["PUT"])
def update_password():
    token = request.headers.get("Authorization")
    before_password = request.json['before_password'] if request.json['before_password'] else ""
    new_password = request.json['new_password'] if request.json['new_password'] else ""
    return jsonify(message=reset_password(before_password, new_password, token))


@mod.route("/verify/<types>/<code>", methods=["GET"])
def verify_code(types, code):
    return jsonify(message=verify_code_phone(types, code))


@mod.route("/auth", methods=["POST"])
def generator_code():
    phone = request.json['phone'] if request.json['phone'] else ""
    types = request.json['type'] if request.json['type'] else ""
    code = generator_code_phone(phone, types)
    if code == 'you already received code':
        return jsonify(message='you already received code')
    else:
        return jsonify(message=code)
