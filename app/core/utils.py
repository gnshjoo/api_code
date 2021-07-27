import bcrypt


def hashed_password(password):
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed.decode("utf-8")


def verify_password(plain_password, hash_password):
    return bcrypt.checkpw(plain_password.encode("utf-8"), hash_password)
