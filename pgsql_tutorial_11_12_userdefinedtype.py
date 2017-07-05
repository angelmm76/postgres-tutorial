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
    # Domain is a data type with optional constraints. Domains are useful for
    # centralizing management of fields with the common constraints
#    cur.execute("""CREATE TABLE mail_list (ID SERIAL PRIMARY KEY,
#            first_name VARCHAR NOT NULL, last_name VARCHAR NOT NULL,
#            email VARCHAR NOT NULL,
#            CHECK (first_name !~ '\s' AND last_name !~ '\s'))""")
    cur.execute("""CREATE DOMAIN contact_name AS 
                VARCHAR NOT NULL CHECK (value !~ '\s')""")
    cur.execute("""CREATE TABLE mail_list (id serial PRIMARY KEY,
            first_name contact_name,  last_name contact_name,
            email VARCHAR NOT NULL)""")
#    cur.execute("""INSERT INTO mail_list (first_name, last_name, email)
#            VALUES ('Jame V', 'Doe', 'jame.doe@example.com')""") # Error!
    # CREATE TYPE statement allows you to create a composite type, which can
    # be used as the return type of a function
    cur.execute("""CREATE TYPE film_summary AS (film_id INT,
            title VARCHAR, release_year YEAR)""")
    cur.execute("""CREATE OR REPLACE FUNCTION get_film_summary (f_id INT) 
            RETURNS film_summary AS $$ 
            SELECT film_id, title, release_year FROM film
            WHERE film_id = f_id ; $$ LANGUAGE SQL""")
    cur.execute("SELECT * FROM get_film_summary (40)")

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