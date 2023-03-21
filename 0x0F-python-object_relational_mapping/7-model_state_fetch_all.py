#!/usr/bin/python3
"""
This codebase write a script
that lists all State objects from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

"""
if makses the files in-executble when imported.
"""

if __name__ == "__main__":
	engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(sys.argv[1], sys.argv[2], sys.argv[3]))

	#Create all Tables associated with the Base metadata
	Base.metadata.create_all(engine)

	# Creating a new Session instance bound to the engine we created
	Session = sessionmaker(bind=engine)
	session = Session()

	# Interacting with the database by query all state objects from the database and order by states.id

	states_list = session.query(State).order_by(State.id).all()

	# Looping through states_list to get the list of states
	for state in states_list:
		print("{}: {}".format(state.id, state.name))

	# closing the session
	session.close()
