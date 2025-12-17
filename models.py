import datetime
from database import Base
from sqlalchemy import Column, Integer, String, DateTime

class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    display_name = Column(String)
    email = Column(String, unique=True)
    password_hash = Column(String)
    password_salt = Column(String)
    created_at = Column(DateTime)