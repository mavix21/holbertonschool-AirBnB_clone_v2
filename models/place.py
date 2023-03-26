#!/usr/bin/python3
""" Place Module for HBNB project """
from .base_model import BaseModel, Base
from .review import Review
from .amenity import Amenity
from sqlalchemy import Column, Table, Integer, String, ForeignKey, Float
from sqlalchemy.orm import relationship
import os

if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
    place_amenity = Table(
            'place_amenity',
            Base.metadata,
            Column(
                'place_id',
                String(60),
                ForeignKey('places.id'),
                nullable=False,
                primary_key=True
                ),
            Column(
                'amenity_id',
                String(60),
                ForeignKey('amenities.id'),
                nullable=False,
                primary_key=True
                )
            )


class Place(BaseModel, Base):
    """ A place to stay """
    if os.environ.get('HBNB_TYPE_STORAGE') == 'db':
        __tablename__ = "places"
        city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        number_rooms = Column(Integer, nullable=False, default=0)
        number_bathrooms = Column(Integer, nullable=False, default=0)
        max_guest = Column(Integer, nullable=False, default=0)
        price_by_night = Column(Integer, nullable=False, default=0)
        latitude = Column(Float)
        longitude = Column(Float)
        reviews = relationship("Review", backref="place", cascade="all")
        amenities = relationship("Amenity",
                                 secondary="place_amenity",
                                 backref="place_amenity",
                                 viewonly=False)
    else:
        city_id = ""
        user_id = ""
        name = ""
        description = ""
        number_rooms = 0
        number_bathrooms = 0
        max_guest = 0
        price_by_night = 0
        latitude = 0.0
        longitude = 0.0
        amenity_ids = []

        @property
        def reviews(self):
            """The reviews property."""
            import models
            return [review for review in models.storage.all(Review).values()
                    if review.place_id == self.id]

        @property
        def amenities(self):
            """The amenities property."""
            import models
            return [amenity for amenity in models.storage.all(Amenity).values()
                    if amenity.id in self.amenity_ids]

        @amenities.setter
        def amenities(self, value):
            if type(value) is not Amenity:
                return

            self.amenity_ids.append(value.id)
