#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

storage_type = os.environ.get('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    from .engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
else:
    from .engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
