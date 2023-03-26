#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime
from datetime import datetime
import os

storage_type = os.environ.get('HBNB_TYPE_STORAGE')
if storage_type == 'db':
    Base = declarative_base()
else:
    Base = object


class BaseModel:
    """A base class for all hbnb models"""
    if storage_type == 'db':
        id = Column(String(60), unique=True, nullable=False, primary_key=True)
        created_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())
        updated_at = Column(DateTime, nullable=False,
                            default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            if not kwargs.get('id'):
                self.id = str(uuid.uuid4())

            if kwargs.get('created_at'):
                kwargs['created_at'] = datetime.fromisoformat(
                        kwargs['created_at'])
            else:
                self.created_at = datetime.now()

            if kwargs.get('updated_at'):
                kwargs['updated_at'] = datetime.fromisoformat(
                        kwargs['updated_at'])
            else:
                self.updated_at = datetime.now()

            if kwargs.get('__class__'):
                del kwargs['__class__']

            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        my_dict = {k: v for k, v in self.to_dict().items() if k != '__class__'}
        cls = self.to_dict().get('__class__')
        return '[{}] ({}) {}'.format(cls, self.id, my_dict)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        try:
            storage.save()
        except Exception as e:
            raise e

    def delete(self):
        """Deletes the current instance from the storage"""
        from models import storage
        try:
            storage.delete(self)
        except KeyError:
            print("** no instance found **")

    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()

        if '_sa_instance_state' in dictionary:
            del dictionary['_sa_instance_state']

        return dictionary
