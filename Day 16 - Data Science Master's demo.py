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
mycursor.execute("SHOW DATABASES")
for x in mycursor:
  print(x)