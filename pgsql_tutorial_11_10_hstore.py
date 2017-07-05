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
    # Store data in key-value pairs
    # Load extension
    cur.execute("CREATE EXTENSION hstore")
    # Create table
    cur.execute("""CREATE TABLE books (id serial primary key,
             title VARCHAR (255), attr hstore)""")
    cur.execute("""INSERT INTO books (title, attr) VALUES (
            'PostgreSQL Tutorial',
            '"paperback" => "243", "publisher" => "postgresqltutorial.com",
            "language"  => "English", "ISBN-13"   => "978-1449370000",
            "weight"    => "11.2 ounces"')""")
    cur.execute("""INSERT INTO books (title, attr) VALUES (
            'PostgreSQL Cheat Sheet',
             '"paperback" => "5", "publisher" => "postgresqltutorial.com",
                "language"  => "English", "ISBN-13"   => "978-1449370001",
                "weight"    => "1 ounces"')""")
    cur.execute("SELECT attr FROM books")
    # Query specific key
    cur.execute("SELECT attr -> 'ISBN-13' AS isbn FROM books")
    cur.execute("""SELECT attr -> 'weight' AS weight FROM books
                    WHERE attr -> 'ISBN-13' = '978-1449370000'""")
    # Add key-value pair to existing row
    cur.execute("""UPDATE books
                SET attr = attr || '"freeshipping"=>"yes"' :: hstore""")
    cur.execute("""SELECT title, attr -> 'freeshipping' AS freeshipping 
                FROM  books""")
    # Update existing key-value pair
    cur.execute("""UPDATE books
                SET attr = attr || '"freeshipping"=>"no"' :: hstore""")
    # Remove existing key-value pair
    cur.execute("""UPDATE books 
                SET attr = delete(attr, 'freeshipping')""")
    # Check for a specific key
    cur.execute("""SELECT title, attr->'publisher' as publisher, attr
                    FROM books WHERE attr ? 'publisher'""")
    cur.execute("""SELECT title FROM books WHERE
                attr ?& ARRAY [ 'language', 'weight' ]""")
    # Check for a key value pair
    cur.execute("""SELECT title FROM books 
                WHERE attr @> '"weight"=>"11.2 ounces"' :: hstore""")
    # Get all keys from a hstore column
    cur.execute("SELECT akeys (attr) FROM books")
    cur.execute("SELECT skeys (attr) FROM books")
    # Get all values from a hstore column
    cur.execute("SELECT avals (attr) FROM books")
    cur.execute("SELECT svals (attr) FROM books")
    # Convert hstore to JSON/dict
    cur.execute("SELECT title, hstore_to_json (attr) json FROM books")
    # Convert hstore data to sets
    cur.execute("SELECT title, (EACH(attr) ).* FROM books")

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