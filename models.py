from pydantic import BaseModel

from sqlalchemy import Column, Integer,String

from database import Base

class UserDB(Base):
    __tablename__="users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String)
    age = Column(Integer)
    email=Column(String,nullable=False)
    password = Column(String, nullable=False)
    role = Column(String, default="user")


class User(BaseModel):
    name: str
    age: int
    email: str
    password: str                                                                                                                    