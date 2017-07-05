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
###### Select columns from table
    cur.execute("SELECT * from customer") # all columns
    cur.execute("SELECT last_name, email FROM customer") # some columns
    cur.execute("""SELECT first_name, last_name FROM customer 
                ORDER BY first_name ASC, last_name DESC""") # ordering 
##### Fetch all queried rows
    rows = cur.fetchall()
    print("\nShow customers:")
    print([desc[0] for desc in cur.description])# headers
    for row in rows:
        print(row)
    
except psycopg2.DatabaseError as e:
    print('Error %s' % e)
    sys.exit(1)
      
finally:
###### Close connection
    if con:
        con.close()