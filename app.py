from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home3")
@app.route("/home")
def home():
    return "this is app.py file"
