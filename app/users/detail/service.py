from app.DB.models import Users
from app.DB.database import db_session
from sqlalchemy.orm.exc import NoResultFound
from app.utils.jwt import verify_token


def get_detail(token):
    user = verify_token(token)
    if user:
        try:
            user_info = db_session.query(Users).filter(Users.email == user).one()
            return {
                "email": user_info.email,
                "name": user_info.name,
                "nickname": user_info.nickname,
                "phone": user_info.phone,
            }
        except NoResultFound:
            return "user_not_found"
    else:
        return "token is expired, please login again"
