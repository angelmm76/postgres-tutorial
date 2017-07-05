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
# Boolean type
    cur.execute("""CREATE TABLE stock (
            product_id INT NOT NULL PRIMARY KEY,
            available BOOLEAN)""")
    cur.execute("""INSERT INTO stock (product_id, available)
        VALUES (1, TRUE), (2, FALSE), (3, 't'), (4, '1'), (9, NULL),
         (5, 'y'), (6, 'yes'), (7, 'no'),  (8, '0'), (10, 'true')""")
    cur.execute("SELECT * FROM  stock")

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