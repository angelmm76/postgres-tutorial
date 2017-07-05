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
# A foreign key in a table refers to a primary key of another table
    # Parent table
    cur.execute("""CREATE TABLE so_headers (id serial PRIMARY KEY,
             customer_id int8, ship_to VARCHAR (255))""")
    # Child table
    cur.execute("""CREATE TABLE so_items (item_id int4 NOT NULL,
         so_id int4, product_id int4, qty int4,
         net_price numeric, PRIMARY KEY (item_id, so_id),
         FOREIGN KEY (so_id) REFERENCES so_headers (ID)) ON DELETE RESTRICT""")
# What happens to the rows in the child table if a row in the parent is deleted?
# ON DELETE RESTRICT: not deleted, the child rows must be deleted first
# ON DELETE DASCADE: the child rows are also deleted
# NO ACTION: raise an error

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