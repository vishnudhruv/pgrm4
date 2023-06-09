import mysql.connector
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="correctpassword",
  database="oneteam"
)
mycursor = mydb.cursor()
addr=()
sql = "SELECT * FROM employee WHERE place = %s"
key=input("enter an address :")
addr = addr+(key, )
mycursor.execute(sql,addr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
