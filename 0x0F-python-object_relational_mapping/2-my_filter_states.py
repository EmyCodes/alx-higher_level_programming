#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
	username=sys.argv[1]
	password=sys.argv[2]
	database=sys.argv[3]
	search_state=sys.argv[4]

	# Make Connection
	conn = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)
	# Load connection
	cursor = conn.cursor()
	sql = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
	cursor.execute(sql, (search_state,))
	states = cursor.fetchall()
	for state in states:
		print(state)

	cursor.close()
	conn.close()
