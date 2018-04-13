from flask import Flask

from flask import render_template

app = Flask(__name__)


@app.route("/")
def hello():
    return render_template("homepage.html")

@app.route("/task")
def taks():
    return render_template("task.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

if __name__ == '__main__':
    app.run(debug=True)
