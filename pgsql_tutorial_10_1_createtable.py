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
###### Create table
    cur.execute("""CREATE TABLE account(
                 user_id serial PRIMARY KEY,
                 username VARCHAR (50) UNIQUE NOT NULL,
                 password VARCHAR (50) NOT NULL,
                 email VARCHAR (355) UNIQUE NOT NULL,
                 created_on TIMESTAMP NOT NULL,
                 last_login TIMESTAMP)""")
    cur.execute("""CREATE TABLE role(
                 role_id serial PRIMARY KEY,
                 role_name VARCHAR (255) UNIQUE NOT NULL)""")
# Two-columned primar key and Foreign key constraint
    cur.execute("""CREATE TABLE account_role(
              user_id integer NOT NULL,
              role_id integer NOT NULL,
              grant_date timestamp without time zone,
              PRIMARY KEY (user_id, role_id),
              CONSTRAINT account_role_role_id_fkey FOREIGN KEY (role_id)
                  REFERENCES role (role_id) MATCH SIMPLE
                  ON UPDATE NO ACTION ON DELETE NO ACTION,
              CONSTRAINT account_role_user_id_fkey FOREIGN KEY (user_id)
                  REFERENCES account (user_id) MATCH SIMPLE
                  ON UPDATE NO ACTION ON DELETE NO ACTION)""")

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