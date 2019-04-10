from flask import Flask, render_template, redirect, url_for, request
from flask_mysqldb import MySQL


#def connect():

#    conn = MySQLdb.connect(db="GameChat", host="localhost", user="root", passwd="Dustin2018", port=3306)
#    cur = conn.cursor()
#    return conn, cur



app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Dustin2018'
app.config['MYSQL_DB'] = 'GameChat'

mysql = MySQL(app)



@app.route("/")
def landingpad():
    return render_template("landingpad.html")

@app.route("/createAccount", methods=['GET, POST'])
def createAccount():
    if request.method =="POST":
        details = request.form
        username = details['username']
        password = details['password']
        email = details['email']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO USERS(username, password, email) VALUES (%s, %s, %s)", (username, password, email))
        mysql.connection.commit()
        cur.close()
        return 'success'
	return render_template("createAccount.html",)

@app.route("/welcome")
def welcome():
	return render_template("welcome.html")

@app.route("/accountCreated")
def accountCreated():
	return render_template("accountCreated.html")

@app.route("/forgotPassword")
def forgotPassword():
	return render_template("forgotPassword.html")

@app.route("/testPage")
def testPage():
    return render_template("testPage.html")


@app.route("/anthemHome")
def anthemHome():
    return render_template("anthemHome.html")

@app.route("/leagueHome")
def leagueHome():
    return render_template("leagueHome.html")

@app.route("/destinyHome")
def destinyHome():
    return render_template("destinyHome.html")

@app.route("/hollowKnightHome")
def hollowKnightHome():
    return render_template("hollowKnightHome.html")

@app.route("/mtgHome")
def mtghome():
    return render_template("mtgHome.html")

if __name__ == '__main__':
    app.run(debug=True)
