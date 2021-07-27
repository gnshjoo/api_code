from flask import request, jsonify
from flask_restplus import Namespace, Resource, fields
from sqlalchemy.orm.exc import NoResultFound
from app.db.database import db_session as sql_session
from app.db.users import Users
from app.core.utils import hashed_password
from app.core.jwt import generate_jwt_token

api = Namespace('signup', description="create users")

signup_data = api.model('signup', {
    "email": fields.String,
    "password": fields.String,
    "nickname": fields.String,
    "name": fields.String,
    "phone": fields.String,
})


@api.route("/signup")
class SignUp(Resource):

    @api.doc("create user", body=signup_data)
    def post(self):
        json_data = request.json()
        email = json_data['email']
        password = json_data['password']
        nickname = json_data['nickname']
        name = json_data['name']
        phone = json_data['phone']

        try:
            user = sql_session.query(Users).filter(Users.email == email).one()
            if user is not None:
                return "user already exist"
        except NoResultFound:
            create_user = Users(email=email, password=hashed_password(password), nickname=nickname, name=name,
                                phone=phone)
            sql_session.add(create_user)
            sql_session.commit()

            token = generate_jwt_token(email, name)

            return jsonify({"access_token": token}, status=200)
        except Exception as e:
            print(e)
            return False
