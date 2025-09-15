from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()

class User(Base):
	__tablename__ = "user"

	id = Column(Integer, primary_key=True, autoincrement=True)
	username = Column(String(120), unique=True, nullable=False)
	email = Column(String(120), unique=True, nullable=False)
	passwd = Column(String(120), unique=True, nullable=False)