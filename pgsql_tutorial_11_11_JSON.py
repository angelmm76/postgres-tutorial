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
    cur.execute("""CREATE TABLE orders (ID serial NOT NULL PRIMARY KEY,
                 info json NOT NULL)""")
    cur.execute("""INSERT INTO orders (info) VALUES
      ('{ "customer": "John Doe", "items": {"product": "Beer","qty": 6}}')""")
    cur.execute("""INSERT INTO orders (info) VALUES
        ('{ "customer": "Lily B", "items": {"product": "Diaper","qty": 24}}'),
        ('{ "customer": "Josh W", "items": {"product": "Toy Car","qty": 1}}'),
     ('{ "customer": "Mary C", "items": {"product": "Toy Train","qty": 2}}')""")
    cur.execute("SELECT info FROM orders")
    # Query JSON data
    cur.execute("SELECT info -> 'customer' AS customer FROM orders") # as json
    cur.execute("SELECT info ->> 'customer' AS customer FROM orders")# as text
    cur.execute("""SELECT info -> 'items' ->> 'product' as product 
                FROM orders ORDER BY product""")
    # Filter with json
    cur.execute("""SELECT info ->> 'customer' AS customer FROM orders
            WHERE info -> 'items' ->> 'product' = 'Diaper'""")
    cur.execute("""SELECT info ->> 'customer' AS customer, 
                info -> 'items' ->> 'product' AS product FROM orders WHERE
                CAST (info -> 'items' ->> 'qty' AS INTEGER) = 2""")
    # Apply aggregate functions
    cur.execute("""SELECT 
            MIN (CAST (info -> 'items' ->> 'qty' AS INTEGER)),
            MAX (CAST (info -> 'items' ->> 'qty' AS INTEGER)),
            SUM (CAST (info -> 'items' ->> 'qty' AS INTEGER)),
            AVG (CAST (info -> 'items' ->> 'qty' AS INTEGER)) FROM orders""")
    # JSON functions
    cur.execute("SELECT json_each (info) FROM orders")
    cur.execute("SELECT json_each_text (info) FROM orders")
    cur.execute("SELECT json_object_keys (info->'items') FROM orders")
    cur.execute("SELECT json_typeof (info->'items') FROM orders")
    cur.execute("SELECT json_typeof (info->'items'->'qty') FROM orders")

##### Fetch all queried rows
    rows = cur.fetchall()
    print("\nShow queried data:")
    print([desc[0] for desc in cur.description]) # headers
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