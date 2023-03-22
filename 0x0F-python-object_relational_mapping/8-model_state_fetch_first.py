#!/usr/bin/python3
"""
This source prints the first State object from the database hbtn_0e_usa.
"""

from model_state import Base, State
from sqlalchemy import create_engine
import sys
from sqlalchemy.orm import sessionmaker

#Making the code in-executable
if __name__ == "__main__":
	#Creating Engines
	engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]))

	# creating all tables from the database
	Base.metadata.create_all(engine)

	#Crwating session
	Session = sessionmaker(bind=engine)
	session = Session()

	# Querying into the database to fetch the first object
	first_state = session.query(State).order_by(State.id).first()

	#Display the result
	if first_state is None:
		print("Nothing")
	else:
		print("{}: {}".format(first_state.id, first_state.name))

	#Closing the session
	session.close()
