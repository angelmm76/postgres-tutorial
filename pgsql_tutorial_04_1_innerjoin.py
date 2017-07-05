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
# The INNER JOIN clause returns rows in A table that have the corresponding 
# rows in the B table
    cur.execute("SELECT customer.customer_id, first_name, last_name, email, " +
                "amount, payment_date FROM customer " +
                "INNER JOIN payment ON payment.customer_id = customer.customer_id")
    cur.execute("SELECT customer.customer_id, first_name, last_name, email, " +
              "amount, payment_date FROM customer " +
              "INNER JOIN payment ON payment.customer_id = customer.customer_id " +
              "ORDER BY customer.customer_id")
    cur.execute("SELECT customer.customer_id, first_name, last_name, email, " +
              "amount, payment_date FROM customer " +
              "INNER JOIN payment ON payment.customer_id = customer.customer_id " +
              "WHERE customer.customer_id = 22")
    cur.execute("SELECT customer.customer_id, " + 
                "customer.first_name customer_first_name, " +
                "customer.last_name customer_last_name, " +
                "customer.email, " +
                "staff.first_name staff_first_name, " +
                "staff.last_name staff_last_name, " +
                "amount, payment_date " +
                "FROM customer " +
                "INNER JOIN payment ON payment.customer_id = customer.customer_id " +
                "INNER JOIN staff ON payment.staff_id = staff.staff_id")
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