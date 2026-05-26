from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    chat_id = Column(String)
    user_message = Column(String)
    bot_reply = Column(String)
    timestamp = Column(DateTime, default=datetime.datetime.utcnow)