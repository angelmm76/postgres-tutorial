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
    # Universal Unique Identifier 32 hex digits (128-bit)
    # UUID generator module
    cur.execute('CREATE EXTENSION IF NOT EXISTS "uuid-ossp"')
    # Generate UUID based on MAC address, timestamp and random number
    cur.execute("SELECT uuid_generate_v1()")
    # Generate UUID based on random number
    cur.execute("SELECT uuid_generate_v4()")
    # Create a table
    cur.execute("""CREATE TABLE contacts (
            contact_id uuid DEFAULT uuid_generate_v4(),
            first_name VARCHAR NOT NULL, last_name VARCHAR NOT NULL,
            email VARCHAR NOT NULL,  phone VARCHAR,
            PRIMARY KEY (contact_id))""")
    cur.execute("""INSERT INTO contacts (
        first_name, last_name, email, phone) VALUES
        ('John', 'Smith','john.smith@example.com', '408-237-2345'),
        ('Jane', 'Smith', 'jane.smith@example.com','408-237-2344'),
        ('Alex', 'Smith', 'alex.smith@example.com', '408-237-2343')""")
    cur.execute("SELECT * FROM contacts")

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