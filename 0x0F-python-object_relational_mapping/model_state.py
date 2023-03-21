#!/usr/bin/python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String, create_engine

"""
Write a python file that contains the class definition of a State and an instance Base = declarative_base()
"""

# create engine
Base = declarative_base()

class State(Base):
	"""
	Class inherit Base Model

	__table__: Table name
	id: state's id
	name: state name

	"""
	__tablename__ = "states"
	id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
	name = Column(String(128), nullable=False)
