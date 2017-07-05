import psycopg2
import sys

con = None

try:
    con = psycopg2.connect(database='template1', user='postgres', password='postgres',
                           host = 'localhost', port = "5432") 
    print("Opened database successfully")
    cur = con.cursor()
    cur.execute('SELECT version()')          
    ver = cur.fetchone()
    print(ver)
    cur.execute('SELECT datname from pg_database')
    rows = cur.fetchall()
    print("\nShow me the databases:\n")
    for row in rows:
        print("   ", row[0])
    cur.execute('SELECT * from *')
    rows = cur.fetchall()
    for row in rows:
        print("   ", row[0])
    
except psycopg2.DatabaseError as e:
    print('Error %s' % e)
    sys.exit(1)
      
finally: 
    if con:
        con.close()