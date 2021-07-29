import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Boolean
from app.DB.database import Base


class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(200), primary_key=False, nullable=False)
    nickname = Column(String(200), primary_key=False, nullable=False)
    activate = Column(Boolean, primary_key=False, default=False)
    email = Column(String(200), primary_key=False, nullable=False)
    password = Column(String(200), primary_key=False, nullable=False)
    phone = Column(String(200), primary_key=False, nullable=False)
    created_date = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, name=None, nickname=None, activate=None, email=None, password=None, created_date=None,
                 phone=None):
        self.name = name
        self.nickname = nickname
        self.activate = activate
        self.email = email
        self.password = password
        self.created_date = created_date
        self.phone = phone

    def __repr__(self):
        return '<Id %r / Name %r / Nickname %r / Activate %r / Email %r / Password %r / Created_date %r / Phone %r />' \
               % (self.id, self.name, self.nickname, self.activate, self.email, self.password, self.created_date,
                  self.phone)

    def __json__(self):
        return ['id', 'name', 'nickname', 'activate', 'email', 'password', 'created_date', 'phone']


class Code(Base):
    __tablename__ = "code"
    id = Column(Integer, primary_key=True, nullable=True)
    phone = Column(String(200), primary_key=False, nullable=False)
    code = Column(String(200), primary_key=False, nullable=False)
    type = Column(String(200), primary_key=False, nullable=False)
    created_date = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, phone=None, code=None, create_date=None, type=None):
        self.phone = phone
        self.code = code
        self.created_date = create_date
        self.type = type

    def __repr__(self):
        return '<Id %r / phone %r / code %r / Created_date %r / Type %r />' \
               % (self.id, self.phone, self.code, self.created_date, self.type)

    def __json__(self):
        return ['id', 'code', 'phone', 'type', 'create_date']
