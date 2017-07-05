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
# The INTERSECT operator returns the common rows in the both result sets of two
# or more SELECT statements. Both queries must return the same number of columns
# and the corresponding columns in the queries must have compatible data types.
# Create two tables for demonstration:
    cur.execute("CREATE TABLE employees (" +
                "employee_id serial PRIMARY KEY, " +
                "employee_name VARCHAR (255) NOT NULL)")
    cur.execute("CREATE TABLE keys (" +
                "employee_id INT PRIMARY KEY, " +
                "effective_date DATE NOT NULL, " +
                "FOREIGN KEY (employee_id) REFERENCES employees (employee_id))")
    cur.execute("CREATE TABLE hipos (" +
                "employee_id INT PRIMARY KEY, " +
                "effective_date DATE NOT NULL, " +
                "FOREIGN KEY (employee_id) REFERENCES employees (employee_id))")
    cur.execute("INSERT INTO employees (employee_name) " +
                "VALUES ('Joyce Edwards'), ('Diane Collins'), ('Alice Stewart'), " +
                "('Julie Sanchez'), ('Heather Morris'), ('Teresa Rogers'), " +
                "('Doris Reed'), ('Gloria Cook'), ('Evelyn Morgan'), ('Jean Bell')")
    cur.execute("INSERT INTO keys " +
                "VALUES  (1, '2000-02-01'), (2, '2001-06-01'), " + 
                "(5, '2002-01-01'), (7, '2005-06-01')")
    cur.execute("INSERT INTO hipos " +
                "VALUES   (9, '2000-01-01'), (2, '2002-06-01'), " +
                "(5, '2006-06-01'), (10, '2005-06-01')")
    cur.execute("SELECT employee_id FROM keys")
    cur.execute("SELECT employee_id FROM hipos")
    cur.execute("SELECT employee_id FROM keys " +
                "INTERSECT SELECT employee_id FROM hipos")
    cur.execute("SELECT employee_id FROM keys " +
                "INTERSECT SELECT employee_id FROM hipos " + 
                "ORDER BY employee_id")

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