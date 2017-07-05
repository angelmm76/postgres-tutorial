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
# Insert new rows into a existing table
# Create a table for demostration
    cur.execute("CREATE TABLE link (" +
                "ID serial PRIMARY KEY, url VARCHAR (255) NOT NULL, " +
                "name VARCHAR (255) NOT NULL, description VARCHAR (255), " +
                "rel VARCHAR (50))")
    cur.execute("INSERT INTO link (url, name) " + # one row
                "VALUES ('www.postgresqltutorial.com','PostgreSQL Tutorial')")
    cur.execute("SELECT * FROM link")
    cur.execute("INSERT INTO link (url, name) " + # another row
                "VALUES ('www.bbc.com','BBC')")
    cur.execute("SELECT * FROM link")
    cur.execute("INSERT INTO link (url, name) " + # multiple rows
                "VALUES ('www.google.com','Google'), " +
                "('www.yahoo.com','Yahoo'), ('www.bing.com','Bing')")
    cur.execute("SELECT * FROM link")
    cur.execute("ALTER TABLE link ADD COLUMN last_update DATE")
    cur.execute("ALTER TABLE link ALTER COLUMN last_update " +
                "SET DEFAULT CURRENT_DATE")
    cur.execute("INSERT INTO link (url, name, last_update) " +
                "VALUES ('www.facebook.com','Facebook','2013-06-01'), " +
                "('www.tumblr.com','Tumblr',DEFAULT)") # insert default
    cur.execute("SELECT * FROM link")
    cur.execute("CREATE TABLE link_tmp (LIKE link)") # insert from another table
    cur.execute("INSERT INTO link_tmp SELECT * FROM link " +
                "WHERE last_update IS NOT NULL")
    cur.execute("SELECT * FROM link_tmp")
    cur.execute("INSERT INTO link (url, NAME, last_update) " +
                "VALUES('www.python.org','Python',DEFAULT) " +
                "RETURNING id") # Get last inserted id
#    cur.execute("SELECT * FROM link_tmp")
    cur.execute("SELECT * FROM link")

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