#!/usr/bin/python3
'''
MySQLdb
'''
import MySQLdb
import sys

if __name__ == "__main__":
	username=sys.argv[1]
	password=sys.argv[2]
	database=sys.argv[3]
	search_state=sys.argv[4]

	# Make Connection
	conn = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)
	# Load connection
	cursor = conn.cursor()
	sql = "SELECT * FROM states WHERE name LIKE '{}%' ORDER BY id ASC".format(search_state[0].capitalize())
	cursor.execute(sql)
	states = cursor.fetchall()
	for state in states:
		print(state)

	cursor.close()
	conn.close()
