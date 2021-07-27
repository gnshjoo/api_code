import jwt
from functools import wraps
from flask import request, Response

encryption_secret = "ably"
algorithm = "HS256"


def generate_jwt_token(email, name):
    data = {"email": email, "name": name}
    encoded = jwt.encode(data, encryption_secret, algorithm=algorithm)
    return encoded


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        access_token = request.headers.get("Authorization")
        if access_token is not None:
            try:
                payload = jwt.decode(access_token, encryption_secret, algorithm=algorithm)
            except jwt.InvalidTokenError:
                payload = None

            if payload is None:
                return Response(status=401)

        else:
            return Response(status=401)

        return f(*args, **kwargs)

    return decorated_function
