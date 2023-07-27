import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost", # or we can use IP address of local system (127.0.0.1)
  user="abc",
  password="password"
)
print(mydb)
mycursor = mydb.cursor()  #mydb is the conectivity
mycursor.execute("CREATE DATABASE if not exists test1")
mycursor.execute("CREATE TABLE if not exists test1.test_table(c1 INT,c2 VARCHAR(50),c3 INT, c4 FLOAT,c5 VARCHAR(40))")
mydb.close()