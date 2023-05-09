import mysql.connector
mydb = mysql.connector.connect(host="loclhost",user='root',passwd='Karan#@0786', database="testing")
mycursor = mydb.cursor()
mycursor.execute("select * from student")

myresult = mycursor.fetchall()

for i in mycursor:
	print(i)
   
        