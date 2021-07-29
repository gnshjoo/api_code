import bcrypt


def hashed_password(password):
    hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
    return hashed.decode("utf-8")


def check_password(plain_pass, hashed_pass):
    hashed = bcrypt.checkpw(plain_pass.encode("utf-8"), hashed_pass.encode("utf-8"))
    return hashed

