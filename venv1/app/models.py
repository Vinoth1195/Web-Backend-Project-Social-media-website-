from fastapi import FastAPI
from .databaseintialize import Base
from sqlalchemy import TIMESTAMP, Column, ForeignKey, Integer, String, Boolean, null,text
from sqlalchemy.orm import relationship
class Posts2(Base):
    __tablename__ = "Posts2"
    id = Column(Integer, primary_key=True, nullable=True)
    title = Column(String, nullable=False)
    content=Column(String, nullable=True)
    published=Column(Boolean, server_default='True', nullable=False)
    timestamp= Column(TIMESTAMP(timezone=True), nullable=False, server_default=(text('NOW()')))
    owner_id= Column(Integer, ForeignKey("Users.id", ondelete="CASCADE"), nullable=False)
    owner = relationship("Users")

class Users(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, nullable=False)
    email= Column(String, nullable=False)
    password= Column(String, nullable= False)
    timestamp= Column(TIMESTAMP(timezone=True), nullable=False, server_default=(text('NOW()')))


class Vote(Base):
    __tablename__="Votes"
    user_id = Column(Integer,ForeignKey("Users.id", ondelete="CASCADE"), primary_key= True, nullable= False)
    post_id= Column(Integer, ForeignKey("Posts2.id", ondelete="CASCADE"), primary_key=True, nullable= False)