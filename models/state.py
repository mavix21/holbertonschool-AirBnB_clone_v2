#!/usr/bin/python3
""" State Module for HBNB project """
from .base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from .city import City
import os


class State(BaseModel, Base):
    """ State class """

    if os.environ.get('HBNB_TYPE_STORAGE') == "db":
        __tablename__ = "states"
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all")
    else:
        name = ""

        @property
        def cities(self):
            return [city for city in models.storage.all(City).values()
                    if city.state_id == self.id]

# City.state = relationship("State", back_populates="cities")
