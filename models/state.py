#!/usr/bin/python3
""" State Module for HBNB project """
import os
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)
    cities = relationship(City, backref='state', cascade='all, delete')

    if (os.getenv('HBNB_TYPE_STORAGE') != 'db'):
        @property
        def cities(self):
            """ returns the list of City instances with state_id equals to the current State.id => It will be the FileStorage relationship between State and City"""
            city_list = []
            from models import storage
            from models.city import City
            for key, value in storage.all(City).items():
                if (self.id == value.state_id):
                    city_list.append(value)
            return city_list
