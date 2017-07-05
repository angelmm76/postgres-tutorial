########### PostgreSQL Tutorial: http://www.postgresqltutorial.com  ##########
import psycopg2
import sys

con = None

def showrows(rows):
    for row in rows:
        print(row)

try:
    con = psycopg2.connect(database='dvdrental', user='postgres', password='postgres',
                           host = 'localhost', port = "5432") 
    print("Opened database successfully")
    cur = con.cursor()
    cur.execute('SELECT version()')          
    ver = cur.fetchone() # fetch a row
    print(ver)
    
    cur.execute("SELECT datname from pg_database")
    rows = cur.fetchall()
    print("\nShow databases:")
    print([desc[0] for desc in cur.description])# headers
    showrows(rows)
    
    cur.execute("""SELECT * FROM pg_catalog.pg_tables 
                WHERE schemaname != 'pg_catalog' AND 
                schemaname != 'information_schema'""")
    rows = cur.fetchall()
    print("\nShow tables:")
    showrows(rows)
    
    cur.execute("""SELECT COLUMN_NAME FROM information_schema.COLUMNS 
                WHERE TABLE_NAME = 'city'""")
    rows = cur.fetchall()
    print("\nDescribe table:")
    showrows(rows)
    
except psycopg2.DatabaseError as e:
    print('Error %s' % e)
    sys.exit(1)
      
finally: 
    if con:
        con.close()