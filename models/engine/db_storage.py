#!/usr/bin/python3
""" Defines the class DBStorage """

import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

mysql_user = os.environ.get('HBNB_MYSQL_USER')
mysql_pwd = os.environ.get('HBNB_MYSQL_PWD')
mysql_host = os.environ.get('HBNB_MYSQL_HOST')
mysql_db = os.environ.get('HBNB_MYSQL_DB')
conn = f"mysql+mysqldb://{mysql_user}:{mysql_pwd}@{mysql_host}/{mysql_db}"


class DBStorage:
    """This class manages storage of hbnb models usign the sqlalchemy ORM"""
    __engine = None
    __session = None
    classes = {
               'User': User,
               # 'Place': Place,
               'State': State,
               'City': City,
               # 'Amenity': Amenity,
               # 'Review': Review
              }

    def __init__(self):
        self.__engine = create_engine(conn, pool_pre_ping=True)

        if mysql_db == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        if not self.__session:
            print("No session established")
            return {}

        try:
            objs = []
            if not cls:
                for _class in DBStorage.classes.values():
                    query = self.__session.query(_class).all()
                    objs.extend(query)
            else:
                objs.extend(self.__session.query(cls).all())

            return {type(obj).__name__ + '.' + obj.id: obj for obj in objs}

        except Exception as e:
            print("Error: {}".format(str(e)))
            return {}

    def new(self, obj):
        if not self.__session:
            print("No session established")
            return

        self.__session.add(obj)

    def save(self):
        if not self.__session:
            print("No session established")
            return

        try:
            self.__session.commit()
        except Exception as e:
            msg_0 = str(e).partition('\n')[0]
            print(msg_0 if msg_0 else str(e))
            self.__session.rollback()
            raise e

    def delete(self, obj=None):
        if self.__session and obj:
            # self.__session.delete(obj)
            Session = sessionmaker(bind=self.__engine)
            session1 = Session.object_session(obj)
            if session1:
                session1.delete(obj)

    def reload(self):
        try:
            Base.metadata.create_all(self.__engine)
            session_factory = sessionmaker(bind=self.__engine,
                                           expire_on_commit=False)
            Session = scoped_session(session_factory)
            self.__session = Session()
        except Exception as e:
            try:
                msg_0 = str(e).split('\n')[0]
                # msg = msg_0.split(" ", 1)[1].split(",")[1].strip()[1:-2]
                print(msg_0)
            except Exception:
                print("Error: {}".format(str(e)))
            finally:
                if self.__session:
                    try:
                        self.__session.close()
                    except Exception as e:
                        print("Error: {}".format(str(e)))
                exit(1)
