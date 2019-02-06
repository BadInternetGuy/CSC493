from flask import Flask
app = Flask(__name__)

@app.route("/")
def landingpad():
    return render_template("landingpad.html")

@app.route("/createAccount")
def createAccount():
	return render_template("createAccount.html")

@app.route("/accountCreated")
def accountCreated():
	return render_template("accountCreated.html")

@app.route("/forgotPassword")
def forgotPassword():
	return render_template("forgotPassword.html")

@app.route("/
if __name__ == "__main__":
    app.run
