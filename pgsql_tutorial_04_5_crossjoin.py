########### PostgreSQL Tutorial: http://www.postgresqltutorial.com  ##########
import psycopg2
import sys

con = None

try:
###### Connect to database
    con = psycopg2.connect(database='dvdrental', 
                           user='postgres', password='postgres',
                           host = 'localhost', port = "5432") 
    print("Opened database successfully")
###### Get cursor
    cur = con.cursor()
# A CROSS JOIN clause allows you to produce the Cartesian Product of rows in
# two or more tables. This join does not have any matching condition.
# Create two tables for demonstration:
    cur.execute("CREATE TABLE T1 (label CHAR(1) PRIMARY KEY)")
    cur.execute("CREATE TABLE T2 (score INT PRIMARY KEY)")
    cur.execute("INSERT INTO T1 (label) VALUES ('A'), ('B')")
    cur.execute("INSERT INTO T2 (score) VALUES (1), (2), (3)")
    cur.execute("SELECT * FROM T1")
    cur.execute("SELECT * FROM T2")
    cur.execute("SELECT * FROM T1 CROSS JOIN T2")

##### Fetch all queried rows
    rows = cur.fetchall()
    print("\nShow queried data:")
    for row in rows:
        print(row)
    
except psycopg2.DatabaseError as e:
    print('Error %s' % e)
    sys.exit(1)
      
finally:
###### Close connection
    if con:
        con.close()