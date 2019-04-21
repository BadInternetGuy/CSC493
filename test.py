import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Dustin2018",
  database="GameChat"
)

mycursor = mydb.cursor()

sql = "INSERT INTO USERS (username, password, email) VALUES (%s, %s, %s)"
val = ("theaskid", "Hidsghway", "yeewwwt@gmail.co")
mycursor.execute(sql, val)

mydb.commit()

print(mycursor.rowcount, "record inserted.")



'''
conn, cur = connect()

data = {}
data['email'] = request.form.get('email')
data['password'] = request.form.get('password')
data['username'] = request.form.get('username')

query = "INSERT INTO `USERS` (`email`, `password`, `username`) VALUES ('{0}', '{1}', '{2}')".format(data['email'],data['password'],data['username'])
cur.execute(query)
conn.commit()
conn.close()
'''
