from app.DB.database import db_session as sql_session
from app.DB.models import Users
from app.utils.hashed import check_password
from app.utils.jwt import generator_token


def login_user(email, password):
    user_info = sql_session.query(Users).filter(Users.email == email).one_or_none()
    if user_info is not None:
        if check_password(password, user_info.password):
            return {"access_token": generator_token(email)}
        else:
            return {"message": "password not match"}
    else:
        return {"message": "user not exist"}
