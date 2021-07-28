from app.DB.database import db_session as sql_session
from app.DB.models import Users, Code
from app.utils.hashed import check_password, hashed_password
from app.utils.jwt import verify_token


def reset_password(b_pass, n_pass, token):
    user = verify_token(token)
    try:
        if user:
            user_info = sql_session.query(Users).filter(Users.email == user).one_or_none()
            code = sql_session.query(Code).filter(Code.phone == user_info.phone).filter(
                Code.type == "reset").one_or_none()
            if user_info is not None and code is None:
                if check_password(b_pass, user_info.password):
                    user_info.password = hashed_password(n_pass)
                    sql_session.commit()
                    return "password changed, please login again"
                else:
                    return "password not match"
            else:
                return "Should verify phone"
        else:
            return "user not exist"
    except Exception as e:
        print(e)
        return "Internal Server Error"
