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
# A natural join is a join that creates an implicit join based on the same 
# column names in the joined tables. A natural join can be an inner (default),
# left, or right. If you use the asterisk (*) in the select list, the result
# will contain all the common columns (columns in the both tables that have the
# same name) and every column in the first and second tables that is not a
# common column.
# Create two tables for demonstration:
    cur.execute("CREATE TABLE categories (" +
                "category_id serial PRIMARY KEY, " +
                "category_name VARCHAR (255) NOT NULL)")
    cur.execute("CREATE TABLE products (" +
                "product_id serial PRIMARY KEY, " +
                "product_name VARCHAR (255) NOT NULL, " +
                "category_id INT NOT NULL, " +
                "FOREIGN KEY (category_id) REFERENCES category (category_id))")
    cur.execute("INSERT INTO categories (category_name) " +
                "VALUES ('Smart Phone'), ('Laptop'), ('Tablet')")
    cur.execute("INSERT INTO products (product_name, category_id) " +
                "VALUES ('iPhone', 1), ('Samsung Galaxy', 1), ('HP Elite', 2)," +
                "('Lenovo Thinkpad', 2), ('iPad', 3), ('Kindle Fire', 3)")
    cur.execute("SELECT * FROM categories")
    cur.execute("SELECT * FROM products")
    cur.execute("SELECT * FROM products NATURAL JOIN categories")
# You should avoid using the NATURAL JOIN whenever possible because sometimes 
# it may cause an unexpected result.
    cur.execute("SELECT * FROM city NATURAL JOIN country")
# This query returns an empty result set because both tables also have a common
# column named last_update, which cannot be used for the join. However, the
# NATURAL JOIN clause just uses the last_update column.

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