from flask import Flask, render_template
import os

app = Flask(__name__)

# set up root route
@app.route("/")
def home():
	return render_template("home.html")

# set up root route
@app.route("/world")
def hello_world():
	return "Hello World"

# Get the PORT from environment
port = os.getenv('PORT', '8080')
if __name__ == "__main__":
	app.run(host='0.0.0.0',port=int(port))