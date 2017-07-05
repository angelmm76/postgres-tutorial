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
###### Create table
    cur.execute("""CREATE TABLE link (
                 link_id serial PRIMARY KEY,
                 title VARCHAR (512) NOT NULL,
                 url VARCHAR (1024) NOT NULL UNIQUE)""")
    # Add column
    cur.execute("ALTER TABLE link ADD COLUMN active boolean")
    # Delete column
    cur.execute("ALTER TABLE link DROP COLUMN active")
#    # Delete column and associated objects(views, triggers, procedures...)
#    cur.execute("ALTER TABLE link DROP COLUMN active CASCADE")
    # Rename column
    cur.execute("ALTER TABLE link RENAME COLUMN title TO link_title")
    # Change column type
    cur.execute("ALTER TABLE link ALTER COLUMN url TYPE TEXT")
    # Add default to existing column
    cur.execute("ALTER TABLE link ADD COLUMN target varchar(10)")
    cur.execute("ALTER TABLE link ALTER COLUMN target SET DEFAULT '_blank'")
    # Two-columned primar key and Foreign key constraint
    cur.execute("""INSERT INTO link (link_title, url)
                VALUES ('PSQL Tutorial', 'www.postgresqltutorial.com')""")
    cur.execute("SELECT * FROM link")
    # Add check condition
#    cur.execute("""ALTER TABLE link 
#            ADD CHECK (target IN ('_self', '_blank', '_parent', '_top'))""")
#    cur.execute("""INSERT INTO link(link_title,url,target) 
#        VALUES('SQL','www.sql.org/','whatever')""") # Error!
    # Rename table
    cur.execute("ALTER TABLE link RENAME TO url")
    cur.execute("SELECT * FROM url")

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