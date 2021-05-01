#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """ cities method

        Returns:
        [list]: return the list of City objects from
        storage linked to the current State
        """
        cities_list = []
        for _city in models.storage.all(City).values():
            if _city.state_id == self.id:
                cities_list.append(_city)
        return cities_list
