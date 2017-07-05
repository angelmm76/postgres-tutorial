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
###### Create table and insert data
    cur.execute("""CREATE TABLE contacts(
            id SERIAL PRIMARY KEY, first_name VARCHAR NOT NULL,
            last_name VARCHAR NOT NULL, email VARCHAR NOT NULL UNIQUE)""")
    cur.execute("""INSERT INTO contacts(first_name, last_name, email) 
            VALUES('John','Doe','john.doe@postgresqltutorial.com'),
            ('David','William','david.william@postgresqltutorial.com')""")
    cur.execute("SELECT * FROM contacts")
# Copy table with data
    cur.execute("CREATE TABLE contact_backup AS TABLE contacts")
    cur.execute("SELECT * FROM contact_backup")
# Copy table without data
    cur.execute("CREATE TABLE contact2 AS TABLE contacts WITH NO DATA")
    cur.execute("SELECT * FROM contact2")

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