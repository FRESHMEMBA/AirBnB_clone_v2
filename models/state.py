#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base, Column, String



class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(120), nullable=False)
