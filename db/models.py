from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

# Движок должен создаваться в одном месте - в db_manager.py
Base = declarative_base()

class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    passwd = Column(String(70), nullable=False)