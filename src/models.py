#import os
#import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    username = Column(String(256), nullable=False)
    password = Column(String(16), nullable=False)
    email = Column(String(64), nullable=False)
    favorites_id = Column(Integer, ForeignKey("favorites.id"))

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    favorites = Column(String(32), nullable=False)
    planets_id = Column(Integer, ForeignKey("planets.id"))
    characters_id = Column(Integer, ForeignKey("characters.id"))
    films_id = Column(Integer, ForeignKey("films.id"))


class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    planet_name = Column(String(128), nullable=False)
    diameter = Column(String(64), nullable=False)
    rotation_period = Column(String(64), nullable=False)
    orbital_period = Column(String(64), nullable=False)
    gravity = Column(String(64), nullable=False)
    population = Column(String(64), nullable=False)
    climate = Column(String(64), nullable=False)
    terrain = Column(String(64), nullable=False)
    surface_water = Column(String(64), nullable=False)
    residents = Column(String(64), nullable=False)
    films_id = Column(Integer, ForeignKey("films.id"))


class Characters(Base):
    __tablename__ = "characters"
    id = Column(Integer, primary_key=True)
    characters_name = Column(String(128), nullable=False)
    birth_year = Column(String(32), nullable=False)
    eye_color = Column(String(32), nullable=False)
    hair_color = Column(String(32), nullable=False)
    skin_color = Column(String(32), nullable=False)
    gender = Column(String(32), nullable=False)
    height = Column(String(32), nullable=False)
    homeworld = Column(String(64), nullable=False)
    planets_id = Column(Integer, ForeignKey("planets.id"))
    planets = relationship(Planets)
    films_id = Column(Integer, ForeignKey("films.id"))


class Films(Base):
    __tablename__ = "films"
    id = Column(Integer, primary_key=True)
    title = Column(String(128), nullable=False)
    director = Column(String(64), nullable=False)
    producer = Column(String(64), nullable=False)
    planets_id = Column(Integer, ForeignKey("planets.id"))
    planets = relationship(Planets)
    characters_id = Column(Integer, ForeignKey("characters.id"))
    characters = relationship(Characters)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
