from pydantic import BaseModel

from sqlalchemy import Column, Integer,String

from database import Base

class UserDB(Base):
    __tablename__="users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    age = Column(Integer)


class User(BaseModel):
    id: int
    name: str
    age: int