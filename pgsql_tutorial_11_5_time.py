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
    # Create demonstration table
    cur.execute("""CREATE TABLE shifts (id serial PRIMARY KEY,
                shift_name VARCHAR NOT NULL,
                start_at TIME NOT NULL, end_at TIME NOT NULL)""")
    cur.execute("""INSERT INTO shifts(shift_name, start_at, end_at)
                VALUES('Morning', '08:00:00', '12:00:00'),
              ('Afternoon', '13:00:00', '17:00:00'),
              ('Night', '18:00:00', '22:00:00')""")
    cur.execute("SELECT * FROM shifts")
    # Time zones
    cur.execute("SELECT LOCALTIME")
    cur.execute("SELECT LOCALTIME AT TIME ZONE'UTC-9'")
    # Extract hours, minutes, days...
    cur.execute("""SELECT LOCALTIME,
                EXTRACT (HOUR FROM LOCALTIME) as hour,
                EXTRACT (MINUTE FROM LOCALTIME) as minute, 
                EXTRACT (SECOND FROM LOCALTIME) as second,
                EXTRACT (milliseconds FROM LOCALTIME) as milliseconds""")
    # Arithmetic operations
    cur.execute("SELECT time '10:00' - time '02:00'")
    cur.execute("SELECT LOCALTIME + interval '2 hours'")

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