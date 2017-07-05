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
# Import data
# Create a table for demostration
    cur.execute("CREATE TABLE persons (id serial NOT NULL, " +
                "first_name character varying(50), " +
                "last_name character varying(50), dob date, " +
                "email character varying(255), " +
                "CONSTRAINT persons_pkey PRIMARY KEY (id))")
    cur.execute("SELECT * FROM persons")
    cur.execute("COPY persons(first_name,last_name,dob,email) " +
                "FROM 'C:/Temp/pgsql_tutorial_09_persons.csv' " +
                "DELIMITER ',' CSV HEADER")
    cur.execute("SELECT * FROM persons")
# Export data
    cur.execute("COPY persons TO 'C:/Temp/pgsql_tutorial_09_persons_2.csv' " +
                "DELIMITER ',' CSV HEADER")
    cur.execute("SELECT * FROM persons")
    cur.execute("COPY persons(first_name,last_name,email) " +
                "TO 'C:/Temp/pgsql_tutorial_09_persons_3.csv' " +
                "DELIMITER ',' CSV HEADER")
    cur.execute("SELECT * FROM persons")
    cur.execute("COPY persons(email) " +
                "TO 'C:/Temp/pgsql_tutorial_09_persons_4.csv' " +
                "DELIMITER ',' CSV")
    cur.execute("SELECT * FROM persons")

##### Fetch all queried rows
    rows = cur.fetchall()
    print("\nShow queried data:")
    for row in rows:
        print(row)
    
except psycopg2.DatabaseError as e:
    print('Error %s' % e)
    sys.exit(1)
      
finally:
###### Close connection
    if con:
        con.close()