#!/usr/bin/python3
"""
Write a python file that contains the class definition of a State and an instance Base = declarative_base()
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String, create_engine


# create engine
Base = declarative_base()

class State(Base):
	"""
	Class inherit Base Model

	__tablename__ (str): Table name.
	id (sqlalchemy.Integer): state's id.
	name (sqlalchemy.String): state name.

	"""
	__tablename__ = "states"
	id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
	name = Column(String(128), nullable=False)
