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
    cur.execute("""CREATE TABLE employees (id serial PRIMARY KEY,
             first_name VARCHAR (50), last_name VARCHAR (50),
             birth_date DATE CHECK (birth_date > '1900-01-01'),
             joined_date DATE CHECK (joined_date > birth_date),
             salary numeric CHECK(salary > 0))""")
    cur.execute("""INSERT INTO employees (first_name,last_name,birth_date,
             joined_date, salary) VALUES
             ('John','Doe', '1972-01-01', '2015-07-01', -100000)""") # Error!

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