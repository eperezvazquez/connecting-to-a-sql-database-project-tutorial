import psycopg2 
import pandas as pd

conn = psycopg2.connect(database="d3ip6cns0p2ok7", 
                        user="ddxvrdfvbjvwul", 
                        password="9c73c2d45fe2c2fd13fa768bcc6b93885ad297ea283b3e25d9733ae54c1a4044", 
                        host="ec2-54-157-16-196.compute-1.amazonaws.com", 
                        port="5432") 
cursor = conn.cursor() 
cursor.execute("CREATE TABLE Movies1 (id INT PRIMARY KEY, name VARCHAR(20));") 


#me genero una tabla en heroku
#3) Execute the SQL sentences to insert your data using the SQLAlchemy's execute function
cursor.execute("INSERT INTO Movies1 (id,name) values (1,'O Reilly Media'),(2,'Prueba'),(3,'Ver');")


# 4) Use pandas to print one of the tables as dataframes using read_sql function
result_dataFrame = pd.read_sql("Select * from Movies1;",conn)
print(result_dataFrame)

conn.commit() 
conn.close()

#Link a heroku con una tabla y tres filas