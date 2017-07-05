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
# SMALLINT: 2 bytes, INT: 4 bytes, BIGINT: 8 bytes
# SERIAL: Generates a sequence of non-null integers
# Numeric: precision (numer of digits), scale(decimal digits)
    cur.execute("""CREATE TABLE IF NOT EXISTS products (
            id serial PRIMARY KEY,  name VARCHAR NOT NULL,
            price NUMERIC (5, 2))""")
    cur.execute("""INSERT INTO products (NAME, price)
                VALUES ('Phone',500.215), ('Tablet',500.214)""")
#    cur.execute("""INSERT INTO products (name, price)
#                VALUES ('Phone',1236.2)""")
    cur.execute("""INSERT INTO products (name, price)
                VALUES ('Phone','NaN')""")
    cur.execute("SELECT * FROM products")

##### Fetch all queried rows
    rows = cur.fetchall()
    print("\nShow queried data:")
    print([desc[0] for desc in cur.description])# headers
    for row in rows:
        print(row)
        
####### Close communication
#    cur.close()
####### Commit te changes
#    con.commit()
    
except psycopg2.DatabaseError as e:
    print('Error %s' % e)
    sys.exit(1)
      
finally:
###### Close connection
    if con:
        con.close()