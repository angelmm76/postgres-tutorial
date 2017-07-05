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
# The EXCEPT operator returns distinct rows from the first (left) query that 
# are not in the output of the second (right) query in the both result sets of 
# two or more SELECT statements. Both queries must return the same number of columns
# and the corresponding columns in the queries must have compatible data types.
    cur.execute("SELECT film_id, title FROM film ORDER BY title") # film table
    cur.execute("SELECT distinct inventory.film_id, title FROM inventory " +
                "INNER JOIN film ON film.film_id = inventory.film_id " +
                "ORDER BY title") # films in inventory
    cur.execute("SELECT * FROM inventory")
    cur.execute("SELECT film_id, title FROM film EXCEPT " +
                "SELECT DISTINCT inventory.film_id, title FROM inventory " +
                "INNER JOIN film ON film.film_id = inventory.film_id " +
                "ORDER BY title")   # films not in inventory

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