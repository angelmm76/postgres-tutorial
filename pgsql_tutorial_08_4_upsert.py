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
# Insert a row, if it does not exist, or update it, if it exists
# Create a table for demostration
    cur.execute("CREATE TABLE customers (customer_id serial PRIMARY KEY, " +
                "name VARCHAR UNIQUE, email VARCHAR NOT NULL, "
                "active bool NOT NULL DEFAULT TRUE)")
    cur.execute("INSERT INTO customers (NAME, email) " + 
                "VALUES ('IBM', 'ct@ibm.com'), " +
                "('Microsoft', 'ct@microsoft.com'), ('Intel', 'ct@intel.com')")
    cur.execute("SELECT * FROM  customers")
    cur.execute("INSERT INTO customers (NAME, email) " +
                "VALUES ('Microsoft', 'hotline@microsoft.com') " +
                "ON CONFLICT ON CONSTRAINT customers_name_key DO NOTHING")
    cur.execute("SELECT * FROM  customers")
    cur.execute("INSERT INTO customers (name, email) " +
               "VALUES ('Microsoft', 'hotline@microsoft.com') " +
               "ON CONFLICT (name) DO NOTHING")
    cur.execute("SELECT * FROM  customers")
    cur.execute("INSERT INTO customers (name, email) " +
               "VALUES ('Microsoft Windows', 'win@microsoft.com') " +
               "ON CONFLICT (name) DO NOTHING")
    cur.execute("SELECT * FROM  customers")
    cur.execute("INSERT INTO customers (name, email) " +
                "VALUES ('Microsoft', 'hotline@microsoft.com')" +
                "ON CONFLICT (name) DO UPDATE " +
                "SET email = EXCLUDED.email || ';' || customers.email")
    cur.execute("SELECT * FROM  customers")

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