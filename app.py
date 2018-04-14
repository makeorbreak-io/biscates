import os
from flask import Flask, render_template, jsonify, redirect, url_for, request
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


class RegisterForm(FlaskForm):
    email = EmailField('Email', [DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmar Password', validators=[
        validators.DataRequired(),
        validators.EqualTo('password', message='Passwords devem ser idênticas')
    ])


@app.route("/")
def home():
    tasks = get_all_tasks()
    for task in tasks:
        task.user_info = get_user_by_id(task.user)
    return render_template("homepage.html", tasks=tasks)


@app.route("/login", methods=["GET"])
def login():
    login_form = LoginForm()
    return render_template("login.html", login_form=login_form)


@app.route("/login", methods=["POST"])
def login_post():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        return redirect('/')

    return render_template("login.html", login_form=login_form)


@app.route("/register", methods=["GET"])
def register():
    register_form = RegisterForm()
    return render_template("register.html", register_form=register_form)


@app.route("/register", methods=["POST"])
def register_post():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        return redirect('/')

    return render_template("register.html", register_form=register_form)


@app.route("/task")
def taks():
    task_id = request.args.get('id')
    task = get_task(task_id)
    task.user_info = get_user_by_id(task.user)
    return render_template("task.html", task=task)


@app.route("/profile")
def profile():
    return render_template("profile.html")


if __name__ == '__main__':
    app.run(debug=True)
