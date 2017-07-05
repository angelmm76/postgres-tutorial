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
    cur.execute("""SELECT last_name, first_name FROM customer
                WHERE last_name='Rice' OR first_name='Paul'""") # filters
    cur.execute("""SELECT customer_id, amount, payment_date FROM payment 
               WHERE amount <= 1 OR amount >= 8""")
    cur.execute("""SELECT film_id, title, release_year FROM film  
                ORDER BY film_id LIMIT 10 OFFSET 3""")
    cur.execute("""SELECT first_name, last_name FROM customer 
                WHERE first_name LIKE '%er%'""")
    cur.execute("""SELECT first_name, last_name FROM customer 
                WHERE first_name ILIKE 'BAR%'""")
    cur.execute("""SELECT rental_id, customer_id, return_date FROM rental 
                WHERE customer_id IN (1,2) ORDER BY return_date DESC""")
    cur.execute("""SELECT first_name, last_name FROM customer 
                WHERE customer_id IN (
                    SELECT customer_id FROM rental WHERE 
                    CAST (return_date AS DATE) = '2005-05-27')""") #subquery
#    cur.execute("""SELECT customer_id, payment_id, amount FROM payment 
#                WHERE amount BETWEEN 8 AND 9""")

##### Fetch all queried rows
    rows = cur.fetchall()
    print("\nShow queried data:")
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