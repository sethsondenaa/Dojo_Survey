from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secrect_key = "asdiknooqwerinf345;2rtew8"

@app.route("/")
def index():
	return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
	return render_template("result.html")

app.run(debug=True)