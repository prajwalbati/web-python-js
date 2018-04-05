from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config['SECRET_KEY'] = 'Your Secret Key'

Session(app)


@app.route("/")
def index():
    headline = "Hello, Prajwal!"
    return render_template("index.html", headline=headline)

@app.route("/bye")
def bye():
    headline = "Goodbye!"
    return render_template("index.html", headline=headline)

@app.route("/more")
def more():
	return render_template("more.html")

@app.route("/hello", methods=["POST"])
def hello():
	name = request.form.get("name")
	return render_template("hello.html", name=name)

@app.route("/form", methods=["GET", "POST"])
def form():
	if session.get("notes") is None:
		session["notes"] = []
	if request.method == "POST":
		note = request.form.get("note")
		session["notes"].append(note)

	return render_template("form.html", notes=session["notes"])
