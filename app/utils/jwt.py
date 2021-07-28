import jwt
import time

SECRET_KEY = 'ably'
ALGORITHM = 'HS256'


def generator_token(email):
    now = time.time() + (60 * 60)
    payload = {
        "email": email,
        "expired_time": now
    }

    token = jwt.encode(payload, SECRET_KEY, ALGORITHM)
    return token.decode('utf-8')


def verify_token(token):
    payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
    if payload["expired_time"] > time.time():
        return payload["email"]
    else:
        return False
