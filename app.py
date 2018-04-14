import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from controllers.task_controller import get_all_tasks



@app.route("/")
def hello():
    tasks = get_all_tasks()
    return render_template("homepage.html", tasks=tasks)


@app.route("/task")
def taks():
    return render_template("task.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


if __name__ == '__main__':
    app.run(debug=True)
