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
    cur.execute("""CREATE TABLE person (id serial PRIMARY KEY,
                 first_name VARCHAR (50), last_name VARCHAR (50),
                 email VARCHAR (50) UNIQUE)""")
    cur.execute("""INSERT INTO person(first_name,last_name,email)
            VALUES ('john', 'doe','j.doe@postgresqltutorial.com')""")
    cur.execute("""INSERT INTO person(first_name,last_name,email)
            VALUES ('jack', 'doeh','j.doe@postgresqltutorial.com')""") # Error!

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