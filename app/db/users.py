from sqlalchemy import Column, Integer, DateTime, String
from app.db.database import Base


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    nickname = Column(String(200), nullable=False)
    email = Column(String(200), nullable=False)
    password = Column(String(200), nullable=False)
    phone = Column(String(200), nullable=False)
    created_date = Column(String(200), nullable=False)

    def __init__(self, name=None, nickname=None, email=None, password=None, create_at=None, phone=None):
        self.name = name
        self.nickname = nickname
        self.email = email
        self.password = password
        self.create_at = create_at
        self.phone = phone

    def __repr__(self):
        return '<Id %r / Name %r / Nickname %r / Email %r / Password %r / Create_date %r / Phone %r / >' \
               % (self.id, self.name, self.nickname, self.email, self.password, self.create_at, self.phone)

    def __json__(self):
        return ['id', 'name', 'nickname', 'email', 'password', 'created_date', 'phone']
