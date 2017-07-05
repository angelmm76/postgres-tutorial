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
# char(n): fixed length, varchar(n): variable length, text-varchar: unltd length
    cur.execute("""CREATE TABLE character_tests (
            id serial PRIMARY KEY, x CHAR (1), y VARCHAR (10), z TEXT)""")
#    cur.execute("""INSERT INTO character_tests (x, y, z)
#            VALUES ( 'Yes', 'This is a test for varchar',
#            'This is a very long text for the PostgreSQL text column')""")
#    cur.execute("""INSERT INTO character_tests (x, y, z)
#            VALUES ( 'Y', 'This is a test for varchar',
#            'This is a very long text for the PostgreSQL text column')""")
    cur.execute("""INSERT INTO character_tests (x, y, z)
            VALUES ( 'Y', 'varchar',
            'This is a very long text for the PostgreSQL text column')""")
    cur.execute("SELECT * FROM   character_tests")

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