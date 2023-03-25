#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel
from sqlalchemy.orm import Column, String, Integer, ForeignKey

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"

    city_id = Column(String(60), ForeignKey('Cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('User.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Columne(Integer, nullabel=False)
    number_bathrooms = Columne(Integer, nullabel=False)
    max_guest = Columne(Integer, nullabel=False)
    price_by_night = Columne(Integer, nullabel=False)
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
