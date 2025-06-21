from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, index=True)
    email = Column(String(100), unique=True, index=True)
    hashed_password = Column(String(255))
    role = Column(String(20), default="user")  # 'user' ou 'admin'

class Resource(Base):
    __tablename__ = "resources"
    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    content = Column(Text)
    type = Column(String(20))  # 'article', 'video', 'quiz'

class MoodEntry(Base):
    __tablename__ = "mood_entries"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    mood = Column(String(20))
    note = Column(Text)
    date = Column(DateTime, default=datetime.utcnow)

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    content = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)
