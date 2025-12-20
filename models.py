from database import Base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey


class Users(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    display_name = Column(String)
    email = Column(String, unique=True)
    password_hash = Column(String)
    created_at = Column(DateTime)

class MessageList(Base):
    __tablename__ = 'message_list'
    message_list_id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.user_id"))

class Messages(Base):
    __tablename__ = 'messages'
    message_id = Column(Integer, primary_key=True, index=True)
    message_list_id = Column(Integer, ForeignKey("message_list.message_list_id"))
    message_content = Column(String)
    created_at = Column(DateTime)
    edited_at = Column(DateTime)
    sender_id = Column(Integer)