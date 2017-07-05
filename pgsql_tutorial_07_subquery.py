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
# A subquery is a query nested inside another query
    cur.execute("SELECT film_id, title, rental_rate FROM film " +
                "WHERE rental_rate > (SELECT AVG (rental_rate) FROM film)")
    cur.execute("SELECT film_id, title FROM film " +
                "WHERE film_id IN (" +
                    "SELECT inventory.film_id FROM rental " +
                    "INNER JOIN inventory ON " +
                    "inventory.inventory_id = rental.inventory_id " +
                    "WHERE return_date BETWEEN '2005-05-29' AND '2005-05-30')")
# If the subquery returns any row, the EXISTS operator returns true. If the
# subquery returns no row, the result of EXISTS operator is false.
    cur.execute("SELECT first_name, last_name FROM customer " + 
                "WHERE EXISTS (" + 
                    "SELECT 1 FROM payment WHERE " +
                    "payment.customer_id = customer.customer_id)")

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