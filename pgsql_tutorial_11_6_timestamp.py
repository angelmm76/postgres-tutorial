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
    # Dates yyyy-mm-dd
    cur.execute("""CREATE TABLE employees (
         employee_id serial PRIMARY KEY, first_name VARCHAR (255),
         last_name VARCHAR (355),
         birth_date DATE NOT NULL, hire_date DATE NOT NULL)""")
    cur.execute("""INSERT INTO employees
                (first_name, last_name, birth_date, hire_date)
                VALUES ('Shannon','Freeman','1980-01-01','2005-01-01'),
                ('Sheila','Wells','1978-02-05','2003-01-01'),
                ('Ethel','Webb','1975-01-01','2001-01-01')""")
    cur.execute("SELECT * FROM employees")
    # Current date
    cur.execute("SELECT CURRENT_DATE")
    cur.execute("SELECT TO_CHAR(CURRENT_DATE, 'dd/mm/yyyy')")
    cur.execute("SELECT TO_CHAR(CURRENT_DATE, 'dd Mon yyyy')")
    # Intervals
    cur.execute("""SELECT first_name, last_name, 
                CURRENT_DATE - hire_date as diff FROM employees""")
    # Ages
    cur.execute("""SELECT employee_id, first_name, last_name,
                 AGE(birth_date) FROM employees""")
    # Extract year, quarter, month, week, day
    cur.execute("""SELECT employee_id, first_name, last_name,
             EXTRACT (YEAR FROM birth_date) AS YEAR,
             EXTRACT (MONTH FROM birth_date) AS MONTH,
             EXTRACT (DAY FROM birth_date) AS DAY FROM employees""")

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