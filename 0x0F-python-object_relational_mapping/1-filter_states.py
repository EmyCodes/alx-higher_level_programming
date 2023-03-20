#!/usr/bin/python3
"""
MySQLdb
"""

import MySQLdb

if __name__ == "__main__":
	username=sys.argv[1]
	password=sys.argv[2]
	database=sys.argv[3]

	# Make Connection
	conn = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)
	# Load connection
	cursor = conn.cursor()
	sql = "SELECT * FROM states WHERE BINARY name LIKE 'N%' ORDER BY id ASC"
	cursor.execute(sql)
	states = cursor.fetchall()
	for state in states:
		print(state)

	cursor.close()
	conn.close()
