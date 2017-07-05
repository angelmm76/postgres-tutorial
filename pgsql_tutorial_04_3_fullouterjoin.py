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
# The full outer join combines the results of both left  join and right join.
# If the rows in the joined table do not match, the full outer join sets NULL 
# values for every column of the table that lacks a matching row.
# Create two tables for demonstration
    cur.execute("CREATE TABLE IF NOT EXISTS departments (" +
                "department_id serial PRIMARY KEY, " +
                "department_name VARCHAR (255) NOT NULL)")
    cur.execute("CREATE TABLE IF NOT EXISTS employees ("
                "employee_id serial PRIMARY KEY, " +
                "employee_name VARCHAR (255), " +
                "department_id INTEGER)")
    cur.execute("INSERT INTO departments (department_name) " +
                "VALUES ('Sales'), ('Marketing'), ('HR'), ('IT'), ('Production')")
    cur.execute("INSERT INTO employees (employee_name, department_id) " +
                "VALUES ('Bette Nicholson', 1), ('Christian Gable', 1), " +
                "('Joe Swank', 2), ('Fred Costner', 3), ('Sandra Kilmer', 4), " +
                "('Julia Mcqueen', NULL)")
    cur.execute("SELECT * FROM departments")
    cur.execute("SELECT * FROM employees")
    cur.execute("SELECT employee_name, department_name FROM employees e " +
                "FULL OUTER JOIN departments d " +
                "ON d.department_id = e.department_id")
    cur.execute("SELECT employee_name, department_name FROM employees e " +
                "FULL OUTER JOIN departments d " +
                "ON d.department_id = e.department_id " +
                "WHERE employee_name IS NULL")
    cur.execute("SELECT employee_name, department_name FROM employees e " +
                "FULL OUTER JOIN departments d " +
                "ON d.department_id = e.department_id " +
                "WHERE department_name IS NULL")
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