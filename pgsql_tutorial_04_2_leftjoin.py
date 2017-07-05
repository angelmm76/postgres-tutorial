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
# The LEFT JOIN clause returns all rows in the left table (A) that are combined
#  with rows in the right table (B) even though there is no corresponding rows 
# in the right table (B)
    cur.execute("SELECT film.film_id, film.title, inventory_id FROM film " +
                "LEFT JOIN inventory ON inventory.film_id = film.film_id")
    cur.execute("SELECT film.film_id, film.title, inventory_id FROM film " +
                "LEFT JOIN inventory ON inventory.film_id = film.film_id " +
                "WHERE inventory.film_id IS NULL")

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