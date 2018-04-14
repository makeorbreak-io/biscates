import os
from flask import Flask, render_template, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField
from wtforms.validators import DataRequired, Email
from wtforms.fields.html5 import EmailField
from controllers.task_controller import *

app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class LoginForm(FlaskForm):
    email = EmailField('Email', [DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

@app.route("/")
def hello():
    tasks = get_all_tasks()
    for task in tasks:
        task.user_info = get_user_by_id(task.user)
    return render_template("homepage.html", tasks=tasks)


@app.route("/login")
def login():
    login_form = LoginForm()
    return render_template("login.html", login_form=login_form)


@app.route("/task")
def taks():
    return render_template("task.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")


if __name__ == '__main__':
    app.run(debug=True)
