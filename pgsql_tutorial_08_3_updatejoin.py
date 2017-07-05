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
# Update data of a table based on values in another table
# Create a table for demostration
    cur.execute("CREATE TABLE product_segment (ID SERIAL PRIMARY KEY, " +
                "segment VARCHAR NOT NULL, discount NUMERIC (4, 2))")
    cur.execute("INSERT INTO product_segment (segment, discount) " +
                "VALUES ('Grand Luxury', 0.05), ('Luxury', 0.06), " +
                "('Mass', 0.1)")
    cur.execute("SELECT * FROM product_segment")
    cur.execute("CREATE TABLE product(id serial primary key, " +
                "name varchar not null, price numeric(10,2), " +
                "net_price numeric(10,2), segment_id int not null, " +
                "foreign key(segment_id) references product_segment(id))")
    cur.execute("INSERT INTO product (name, price, segment_id) " +
                "VALUES ('diam', 804.89, 1), ('vestibulum aliquet', 228.55, 3)," +
                "('lacinia erat', 366.45, 2), ('scelerisque quam', 145.33, 3)," +
                "('justo lacinia', 551.77, 2), ('ultrices mattis', 261.58, 3), " +
                "('hendrerit', 519.62, 2), ('in hac habitasse', 843.31, 1)")
    cur.execute("SELECT * FROM product")
    cur.execute("UPDATE product SET net_price = price - price * discount " +
                "FROM product_segment WHERE " +  # Calculate net price
                "product.segment_id = product_segment.id")
    cur.execute("SELECT * FROM product")

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