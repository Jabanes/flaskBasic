
from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/names")
def names():
    with open('names.json') as f:
        peoples = json.load(f)
    return render_template("names.html", peoples = peoples)


@app.route("/name/<name>")
def name_page(name):
    return render_template("name.html", name=name)

if __name__ == "__main__":
    app.run(debug=True)