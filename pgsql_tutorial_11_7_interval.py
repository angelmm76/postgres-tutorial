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
    # Intervals
    cur.execute("""SELECT now(),
                now() - INTERVAL '1 year 3 hours 20 minutes' AS interv ,
                INTERVAL '2 months ago' AS interv""")
    # Arithmetic operations
    cur.execute("SELECT INTERVAL '2h 50m' + INTERVAL '10m'")
    cur.execute("SELECT INTERVAL '2h 50m' - INTERVAL '50m'")
    cur.execute("SELECT 600 * INTERVAL '1 minute'")
    # Interval to string
    cur.execute("SELECT to_char(INTERVAL '17h 20m 05s', 'HH24:MI:SS')")
    # Extract data from intervals
    cur.execute("SELECT EXTRACT (MINUTE FROM INTERVAL '5 hours 21 minutes')")
    # Adjusting intervals
    cur.execute("""SELECT
            justify_days(INTERVAL '35 days'),
            justify_hours(INTERVAL '27 hours')""")
    cur.execute("SELECT justify_interval(interval '1 year -1 hour')")

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