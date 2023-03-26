#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os
from .engine.db_storage import DBStorage
from .engine.file_storage import FileStorage

storage_type = os.environ.get('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()

storage.reload()
