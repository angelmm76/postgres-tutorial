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
# Group returned rows and apply and aggregate function
    cur.execute("SELECT customer_id FROM payment " + 
                "GROUP BY customer_id") # no function, just remove duplicates
    cur.execute("SELECT customer_id, SUM (amount) FROM payment " +
                "GROUP BY customer_id") # sum
    cur.execute("SELECT customer_id, SUM (amount) FROM payment " +
                "GROUP BY customer_id ORDER BY SUM (amount) DESC")
    cur.execute("SELECT customer_id, SUM (amount) FROM payment " +
                "GROUP BY customer_id HAVING SUM (amount) > 150")
    cur.execute("SELECT staff_id, COUNT (payment_id) FROM payment " +
                "GROUP BY staff_id") # count
    cur.execute("SELECT staff_id, COUNT (payment_id) FROM payment " +
                "GROUP BY staff_id HAVING COUNT (payment_id) > 7300")
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