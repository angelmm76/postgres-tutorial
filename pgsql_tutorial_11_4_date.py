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
    # Timestamp with or without time zone
    cur.execute("""CREATE TABLE timestamp_demo 
                    (ts TIMESTAMP, tstz TIMESTAMPTZ)""")
    cur.execute("SET timezone = 'America/Los_Angeles'")
    cur.execute("SHOW TIMEZONE")
    # Current date
    cur.execute("""INSERT INTO timestamp_demo (ts, tstz)
        VALUES ('2016-06-22 19:10:25-07', '2016-06-22 19:10:25-07')""")
    cur.execute("SELECT * FROM timestamp_demo")
    # Change the timezone, change timestamptz
    cur.execute("SET timezone = 'Europe/Madrid'")
    cur.execute("SELECT * FROM timestamp_demo")
    # Current timestamp
    cur.execute("SELECT NOW()")
    cur.execute("SELECT CURRENT_TIMESTAMP")
    # Current time
    cur.execute("SELECT CURRENT_TIME")
    # Current time of day
    cur.execute("SELECT TIMEOFDAY()")
    # Convert between timezones
    cur.execute("SELECT timezone('Africa/Kampala','2016-06-01 23:00')")

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