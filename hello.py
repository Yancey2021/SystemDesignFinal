from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route("/")
def hello_world():
	return render_template('welcome.htm')




