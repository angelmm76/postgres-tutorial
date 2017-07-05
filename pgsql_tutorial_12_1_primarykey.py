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
# Primary key: a column or a group of columns that is used to identify a row
# uniquely in a table. Defined through primary key constraints (notnull+unique)
    cur.execute("""CREATE TABLE po_headers (
         po_no INTEGER PRIMARY KEY, vendor_no INTEGER,
         description TEXT, shipping_address TEXT)""")
    cur.execute("""CREATE TABLE po_items (
         po_no INTEGER, item_no INTEGER, product_no INTEGER,
         qty INTEGER, net_price NUMERIC, PRIMARY KEY (po_no, item_no)
        )""")
    # Add primary to existing table
    cur.execute("""CREATE TABLE products (product_no INTEGER,
             description TEXT, product_cost NUMERIC)""")
    cur.execute("SELECT * FROM products")
#    cur.execute("ALTER TABLE products ADD PRIMARY KEY (product_no)")
    cur.execute("ALTER TABLE products ADD COLUMN ID SERIAL PRIMARY KEY")
#    # Remove primary key constraint
    cur.execute("ALTER TABLE products DROP CONSTRAINT products_pkey")
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