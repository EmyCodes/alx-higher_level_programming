#!/usr/bin/python3
"""
MySQL
"""

import MySQLdb
import sys

if __name__ == "__main__":
	username = sys.argv[1]
	password = sys.argv[2]
	database = sys.argv[3]
	
	conn = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=database)
	# Assign cursor
	cur = conn.cursor()
	sql = "SELECT * FROM states ORDER BY id ASC"
	cur.execute(sql)
	# Get items
	states = cur.fetchall()
	for state in states:
		print(state)
	cur.close()
	conn.close()
