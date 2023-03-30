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
	
	#Adding new state
	new_state = State(name="Louisiana")
	session.add(new_state)
	
	#Commit the session
	session.commit()

	# Interacting with the database by query all state objects that has 'a' as their character  from the database and order by states.id
	state_object = session.query(State).where(State.name == "Louisiana").order_by(State.id).first()

	# Looping through states_list to get the list of states
	if state_object:
		print(state_object.id)
	else:
		print("Not found")
		
	# closing the session
	session.close()