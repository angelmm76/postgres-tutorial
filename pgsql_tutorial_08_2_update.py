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
# Change values of the table
# Create a table for demostration
    cur.execute("CREATE TABLE link (" +
                "ID serial PRIMARY KEY, url VARCHAR (255) NOT NULL, " +
                "name VARCHAR (255) NOT NULL, description VARCHAR (255), " +
                "rel VARCHAR (50), last_update DATE)")
    cur.execute("INSERT INTO link (url, name) " + 
                "VALUES ('www.postgresqltutorial.com','PostgreSQL Tutorial'), " +
                "('www.bbc.com','BBC'), ('www.google.com','Google'), " +
                "('www.yahoo.com','Yahoo'), ('www.bing.com','Bing')")
    cur.execute("ALTER TABLE link ALTER COLUMN last_update " +
                "SET DEFAULT CURRENT_DATE")
    cur.execute("INSERT INTO link (url, name, last_update) " +
                "VALUES ('www.facebook.com','Facebook','2013-06-01'), " +
                "('www.tumblr.com','Tumblr',DEFAULT), " + 
                 "('www.python.org','Python',DEFAULT)")
    cur.execute("CREATE TABLE link_tmp (LIKE link)") # insert from another table
    cur.execute("INSERT INTO link_tmp SELECT * FROM link " +
                "WHERE last_update IS NOT NULL")
    cur.execute("SELECT * FROM link_tmp")
    cur.execute("SELECT * FROM link")
    cur.execute("UPDATE link " + # Change null dates to defaults
                "SET last_update = DEFAULT WHERE last_update IS NULL")
    cur.execute("SELECT * FROM link")
    cur.execute("UPDATE link SET rel = 'nofollow'") # Change all rows
    cur.execute("SELECT * FROM link")
    cur.execute("UPDATE link SET description = name") # Copy values of columns
    cur.execute("SELECT * FROM link")
    cur.execute("UPDATE link_tmp " + # Update values from one table to another
                "SET rel = link.rel, description = link.description, " +
                "last_update = link.last_update FROM link " +
                "WHERE link_tmp.id = link.id")
    cur.execute("SELECT * FROM link_tmp")
    cur.execute("UPDATE link " + # Returns updated entry
                "SET description = 'Learn PGSQL fast and easy', rel = 'follow'" +
                "WHERE ID = 1 RETURNING id, description, rel")
#    cur.execute("SELECT * FROM link")

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