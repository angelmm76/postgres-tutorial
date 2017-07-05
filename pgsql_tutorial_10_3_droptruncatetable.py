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
    # Drop table
#    cur.execute("DROP TABLE author") # Error! the table does not exist
    cur.execute("DROP TABLE IF EXISTS author")
###### Create tables
    cur.execute("""CREATE TABLE author (
             author_id INT NOT NULL PRIMARY KEY,
             firstname VARCHAR (50),
             lastname VARCHAR (50))""")
    cur.execute("""CREATE TABLE page (
             page_id serial PRIMARY KEY, title VARCHAR (255) NOT NULL,
             CONTENT TEXT, author_id INT NOT NULL,
             FOREIGN KEY (author_id) REFERENCES author (author_id))""")
    # Drop table
#    cur.execute("DROP TABLE IF EXISTS author") # Error! page table constraints
    cur.execute("DROP TABLE author CASCADE")
#    cur.execute("SELECT * FROM page")
    # Remove all rows from a table
    cur.execute("TRUNCATE TABLE customer CASCADE")

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