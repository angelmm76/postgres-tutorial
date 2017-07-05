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
# The UNION operator combines result sets of two or more SELECT statements into
# a single result set. Both queries must return the same number of columns and
# the corresponding columns in the queries must have compatible data types.
# Create two tables for demonstration:
    cur.execute("CREATE TABLE sales2007q1 (" +
                "name VARCHAR (255) PRIMARY KEY, " +
                "amount NUMERIC)")
    cur.execute("CREATE TABLE sales2007q2 (" +
                "name VARCHAR (255) PRIMARY KEY, " +
                "amount NUMERIC)")
    cur.execute("INSERT INTO sales2007q1 (name, amount) " +
                "VALUES ('Mike', 15000.25), ('Jon', 12582.5), ('Mary', 10000)")
    cur.execute("INSERT INTO sales2007q2 (name, amount) " +
                "VALUES ('Mike', 13400.25), ('Jon', 12772.5), ('Mary', 10000)")
    cur.execute("SELECT * FROM sales2007q1")
    cur.execute("SELECT * FROM sales2007q2")
    cur.execute("SELECT * FROM sales2007q1 UNION SELECT * FROM sales2007q2")
    cur.execute("SELECT * FROM sales2007q1 " +
                "UNION ALL SELECT * FROM sales2007q2")
    cur.execute("SELECT * FROM sales2007q1 " +
                "UNION ALL SELECT * FROM sales2007q2 " + 
                "ORDER BY name ASC, amount DESC")

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