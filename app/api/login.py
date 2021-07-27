from flask import request, jsonify
from flask_restplus import Namespace, Resource, fields
from app.db.database import db_session as sql_session
from app.db.users import Users
from app.core.utils import verify_password
from sqlalchemy.orm.exc import NoResultFound

api = Namespace('users', description="about users")

login_data = api.model('login', {
    "email": fields.String,
    "password": fields.String,
})


@api.route("/detail/<email>")
class GetUserDetail(Resource):

    @api.doc("get_user")
    def get(self, email):
        try:
            user_info = sql_session.query(Users).filter(Users.email == email).one()

            return jsonify(user_info, status=200)

        except NoResultFound:
            return jsonify("user not found", status=400)


@api.route("/login")
class UserLogin(Resource):

    @api.doc("login", body=login_data)
    def post(self):
        json_data = request.json()
        email = json_data['email']
        password = json_data['password']

        try:
            user = sql_session.query(Users).filter(Users.email == email).one()

            if verify_password(password, user.password):
                return True
            else:
                return "password not match"
        except NoResultFound:
            return "user not exist"
