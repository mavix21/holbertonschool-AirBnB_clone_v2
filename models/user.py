#!/usr/bin/python3
"""This module defines a class User"""
from .base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .place import Place
import os

storage_type = os.environ.get('HBNB_TYPE_STORAGE')


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    if storage_type == 'db':
        __tablename__ = "users"
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128))
        last_name = Column(String(128))
        places = relationship("Place", backref="user", cascade="all")
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
