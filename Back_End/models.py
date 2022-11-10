from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, BigIntegers
from sqlalchemy.orm import relationship

from db import Base

class User(Base):
    __tablename__ = "users" 

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(20), index=True)


class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    date = Column(BigIntegers)
    user_id = Column(Integer, ForeignKey("users.id"))
    description = Column(String(300))
    happiness = Column(Integer)
    likesCount = Column(Integer)
    commentCounts = Column(Integer)