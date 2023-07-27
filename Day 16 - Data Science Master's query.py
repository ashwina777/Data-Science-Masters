import mysql.connector
# import mysql.connector
#create user 'user'@'%' identified by 'password'
mydb = mysql.connector.connect(
  host="localhost", # or we can use IP address of local system (127.0.0.1)
  user="abc",
  password="password"
)
mycursor = mydb.cursor()  #mydb is the conectivity
#mycursor.execute("select * from test1.test_table")
mycursor.execute("select c1,c5 from test1.test_table") # for particular column
for i in mycursor.fetchall():
    print(i)
