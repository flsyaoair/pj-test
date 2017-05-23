# -*- coding: UTF-8 -*- 
from sqlalchemy import Column, ForeignKey
from sqlalchemy.types import String, Integer, CHAR, BIGINT
from sqlalchemy.orm import sessionmaker, relationship
from database import *

class Blog(BaseModel):
    __tablename__ = 'blog'

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    title = Column(String(64), server_default='', nullable=False)
    user = Column(BIGINT, ForeignKey('user.id'), index=True, nullable=False)
    create = Column(BIGINT, index=True, server_default='0', nullable=False)
    
#     user_obj = relationship('User')
    user_obj = relationship('User', lazy='joined')
    


class User(BaseModel):
    __tablename__ = 'user'

    id = Column(BIGINT, primary_key=True, autoincrement=True)
    name = Column(String(32), server_default='', nullable=False)
    username = Column(String(32), index=True, server_default='', nullable=True)
    password = Column(String(64), server_default='', nullable=False)
    
#     blog_list = relationship('Blog', order_by='Blog.create', lazy="dynamic")
    
#     blog_list = relationship('Blog', order_by='Blog.create')
    blog_list = relationship('Blog',
                             cascade='save-update, delete, delete-orphan, merge')
    
    
