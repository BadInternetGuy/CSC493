from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def landingpad():
    return render_template("landingpad.html")

@app.route("/createAccount")
def createAccount():
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
