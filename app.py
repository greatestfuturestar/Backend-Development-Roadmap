from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/python")
def python_page():
    return render_template("python.html")

@app.route("/databases")
def databases():
    return render_template("databases.html")

@app.route("/backend")
def backend():
    return render_template("backend.html")

if __name__ == "__main__":
    app.run(debug=True)