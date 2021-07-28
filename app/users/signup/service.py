import random
from app.DB.models import Code, Users
from app.DB.database import db_session
from app.utils.hashed import hashed_password
from sqlalchemy.orm.exc import NoResultFound


def create_user(email, nickname, name, password, phone):
    try:
        if email == "" or nickname == "" or name == "" or password == "" or phone == "":
            raise Exception
        user_info = db_session.query(Users).filter(Users.phone == phone).filter(Users.activate == "True").one()
        user_info.email = email
        user_info.nickname = nickname
        user_info.name = name
        user_info.password = hashed_password(password)
        db_session.commit()
        return f'{email} user created'
    except NoResultFound:
        return "You don't verify phone"

    except Exception as e:
        print(e)
        return "create User failed"
