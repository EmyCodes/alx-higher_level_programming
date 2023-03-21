#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    # Script arguments
    mysql_user = argv[1]
    mysql_password = argv[2]
    db_name = argv[3]
    state_name = argv[4]

    # Connect to MySQL database
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_user,
        passwd=mysql_password,
        db=db_name
    )

    # Create cursor to execute queries
    cursor = db.cursor()

    # Select all cities of the given state
    cursor.execute("""
        SELECT cities.name FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """, (state_name,))

    # Fetch all rows as a list of tuples and join city names with a comma separator
    cities = [row[0] for row in cursor.fetchall()]
    cities_str = ', '.join(cities)

    # Print the result
    print(cities_str)

    # Close cursor and database connections
    cursor.close()
    db.close()

