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
# Delete rows in a table
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
    cur.execute("CREATE TABLE link_tmp (LIKE link)")
    cur.execute("INSERT INTO link_tmp SELECT * FROM link " +
                "WHERE last_update IS NOT NULL")
    cur.execute("SELECT * FROM link")
#    cur.execute("SELECT * FROM link_tmp")
    cur.execute("DELETE FROM link WHERE ID=8") #Delete one row
    cur.execute("SELECT * FROM link")
    cur.execute("DELETE FROM link USING link_tmp " + # Delete using other table
                "WHERE link.id = link_tmp.id")
    cur.execute("SELECT * FROM link")
    cur.execute("DELETE FROM link") # Delete all rows
    cur.execute("SELECT * FROM link")
    cur.execute("DELETE FROM link_tmp " +  # Delete returning deleted rows
                "RETURNING *")

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