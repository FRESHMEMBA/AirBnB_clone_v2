#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base, Column, String
from sqlalchemy import ForeignKey


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = "cities"
    id = Column(String(60), primary_key=True, nullable=False)
    state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    name = Column(String(120), nullable=False)
