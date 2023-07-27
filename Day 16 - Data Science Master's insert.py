import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost", # or we can use IP address of local system (127.0.0.1)
  user="abc",
  password="password"
)
mycursor = mydb.cursor()  #mydb is the conectivity
mycursor.execute("insert into test1.test_table values(3243,'ashwina',345,34.54,'rawat')")
mycursor.execute("insert into test1.test_table values(3243,'ashwina',345,34.54,'rawat')")
mycursor.execute("insert into test1.test_table values(3243,'ashwina',345,34.54,'rawat')")
mycursor.execute("insert into test1.test_table values(3243,'ashwina',345,34.54,'rawat')")
mycursor.execute("insert into test1.test_table values(3243,'ashwina',345,34.54,'rawat')")
mycursor.execute("insert into test1.test_table values(3243,'ashwina',345,34.54,'rawat')")
mycursor.execute("insert into test1.test_table values(3243,'ashwina',345,34.54,'rawat')")
mycursor.execute("insert into test1.test_table values(3243,'ashwina',345,34.54,'rawat')")
mydb.commit()
mydb.close()