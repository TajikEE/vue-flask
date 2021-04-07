import sys

from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.types import PickleType

from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy.orm import relationship

from sqlalchemy import create_engine

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    sectors = Column(PickleType, nullable=False)
    name = Column(String(250), nullable=False)
    terms = Column(Boolean, unique=False, default=False, nullable=False)

# creates a create_engine instance
engine = create_engine('sqlite:///users-collection.db', echo=True)

Base.metadata.create_all(engine)