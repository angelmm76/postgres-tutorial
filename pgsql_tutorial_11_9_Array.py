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
    # Arrays of every type
    cur.execute("""CREATE TABLE contacts (id serial PRIMARY KEY,
             name VARCHAR (100), phones TEXT [])""")
    cur.execute("""INSERT INTO contacts (name, phones) VALUES
         ('John Doe', ARRAY [ '(408)-589-5846', '(408)-589-5555' ])""")
    cur.execute("SELECT * FROM contacts")
    cur.execute("""INSERT INTO contacts (name, phones) VALUES
         ('Lily Bush', '{"(408)-589-5841"}'),
         ('William Gate','{"(408)-589-5842","(408)-589-58423"}')""")
    cur.execute("SELECT * FROM contacts")
    cur.execute("SELECT name, phones[1] FROM contacts")
    cur.execute("SELECT name FROM contacts WHERE phones[2]='(408)-589-58423'")
    # Modify array
    cur.execute("""UPDATE contacts 
                SET phones [ 2 ] = '(408)-589-5843' WHERE ID = 3""")
    cur.execute("""SELECT id, name, phones [ 2 ] FROM contacts
                WHERE id = 3""")
    cur.execute("""UPDATE contacts SET phones = '{"(408)-119-5843"}'
                WHERE ID = 3""")
    cur.execute("SELECT id, name, phones FROM contacts WHERE id = 3")
    # Search in array
    cur.execute("""SELECT name, phones FROM contacts WHERE
                        '(408)-589-5555' = ANY (phones)""")
    # Expand array to list of rows
    cur.execute("SELECT name, unnest(phones) FROM contacts")

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