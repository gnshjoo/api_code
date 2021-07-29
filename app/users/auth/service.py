import random
from app.DB.models import Code, Users
from app.DB.database import db_session
from sqlalchemy.orm.exc import NoResultFound
from app.utils.logging import logger


def generator_code_phone(phone, types):
    code = ''.join([str(random.randint(0, 999)).zfill(3) for _ in range(2)])
    logger.debug(code)
    try:
        db_session.query(Code).filter(Code.phone == phone).one()
        logger.debug("query")
    except NoResultFound:
        logger.debug("NoResultFound")
        code_insert = Code(phone=phone, code=code, type=types)
        user_info = Users(phone=phone)
        db_session.add(code_insert)
        db_session.add(user_info)
    except Exception as e:
        logger.debug(e)
        return {"message": "you already received code"}
    db_session.commit()
    return {"message": code}


def verify_code_phone(types, code):
    code_info = db_session.query(Code).filter(Code.code == code).filter(Code.type == types).one_or_none()
    if code is not None:
        user = db_session.query(Users).filter(Users.phone == code_info.phone).one()
        user.activate = 1
        db_session.query(Code).filter(Code.code == code).delete()
        db_session.commit()

        return {"message": "phone verified"}

    else:
        return {"message": "code is not verified"}
