import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(200), nullable=False)
    lastName = Column(String(200), nullable=False)
    user_name = Column(String(200))
    email= Column(String(200))
    password= Column(String(200))

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    content = Column(String(200), nullable=False)
    url= Column(String(250))
    post_id= Column(Integer, ForeignKey('post.id'))

class Post(Base):
    __tablename__ = 'post'
    id = Column(String(60), primary_key=True)
    user_id= Column(Integer, ForeignKey('user.id'))


class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    description= Column(String(25000))
    user_id= Column(Integer, ForeignKey('user.id'))
    post_id= Column(Integer, ForeignKey('post.id'))




## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
