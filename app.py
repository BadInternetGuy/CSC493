"""
This is the code for GameChat.
Created by: Dustin Young

Special thanks:

Richard Maiti
Scott Heggen
Mario Nakazawa
Jan Pearce
"""

from flask import Flask, render_template, redirect, url_for, request, session
import MySQLdb
import mysql.connector



# Establish connection to the database.

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="Dustin2018",
  database="GameChat"
)


app = Flask(__name__)



@app.route("/")
def landingpad():
    return render_template("landingpad.html")


#Allows the creation of an account.
@app.route("/createAccount", methods=['GET', 'POST'])
def createAccount():
    mycursor = mydb.cursor()


    sql = "INSERT INTO USERS (username, password, email) VALUES (%s, %s, %s)"
    val = (request.form.get("username"), request.form.get("password"), request.form.get("email"))

    mycursor.execute(sql, val)

    mydb.commit()


    return render_template("createAccount.html")

@app.route("/welcome")
def welcome():
	return render_template("welcome.html")

@app.route("/accountCreated")
def accountCreated():
	return render_template("accountCreated.html")

@app.route("/forgotPassword")
def forgotPassword():
	return render_template("forgotPassword.html")

@app.route("/anthemHome")
def anthemHome():
    return render_template("anthemHome.html")

@app.route("/leagueHome")
def leagueHome():
    return render_template("leagueHome.html")

@app.route("/destinyHome")
def destinyHome():
    return render_template("destinyHome.html")

@app.route("/destinyNav")
def destinyNav():
    return render_template("destinyNav.html")

@app.route("/hollowKnightHome")
def hollowKnightHome():
    return render_template("hollowKnightHome.html")

@app.route("/mtgHome")
def mtghome():
    return render_template("mtgHome.html")

    #Set to debug mode to enable auto-refresh 

if __name__ == '__main__':
    app.run(debug=True)
