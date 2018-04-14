import os
from flask import Flask, render_template, jsonify, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField,TextField, PasswordField, StringField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms.fields.html5 import EmailField
from flask_login import LoginManager


app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)

from controllers.task_controller import *


class LoginForm(FlaskForm):
    email = EmailField('Email', [DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])


class RegisterForm(FlaskForm):
    email = EmailField('Email', [DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmar Password', validators=[
        DataRequired(),
        EqualTo('password', message='Passwords devem ser idênticas')
    ])


class NewProposalForm(FlaskForm):
    user = StringField('Utilizador', [DataRequired()])
    offer = StringField('Preço', [DataRequired()])
    description = TextField('Descrição', [DataRequired()])
    task_id = StringField('task_id',[DataRequired()])
    type = StringField('type', [DataRequired()])


class TaskForm(FlaskForm):
    title = StringField('Job Title')
    location = StringField('Location')
    price = StringField('Proposed Price')
    description = StringField('Job Description')

@app.route("/")
def home():
    tasks = get_all_tasks()
    for task in tasks:
        task.user_info = get_user_by_id(task.user)
    return render_template("homepage.html", tasks=tasks)


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    if login_form.validate_on_submit():
        return redirect('/')

    return render_template("login.html", login_form=login_form)


@app.route("/register", methods=["GET", "POST"])
def register():
    register_form = RegisterForm()
    if register_form.validate_on_submit():
        return redirect('/')

    return render_template("register.html", register_form=register_form)


@app.route("/task/<task_id>")
def task(task_id):
    newproposal_form = NewProposalForm()
    id = float(task_id)
    task = get_task(id)
    task.user_info = get_user_by_id(task.user)
    return render_template("task.html", task=task, newproposal_form=newproposal_form)


@app.route("/profile/<user_id>")
def profile(user_id):
    id = float(user_id)
    user = get_user_by_id(id)
    tasks = get_user_tasks(id)
    for task in tasks:
        task.rating = get_task_rating(task.id)
    return render_template("profile.html", user=user, tasks=tasks)


@app.route("/proposal", methods=['POST'])
def offer():
    type = request.form.get('type')

    if 'create' == type:
        taskID = request.form.get('task_id')
        user = request.form.get('user')
        offer = request.form.get('offer')
        description = request.form.get('description')
        msg = insertProposal(taskID, user, offer, description)
        return redirect("/task/" + taskID)
    else:
        proposalID = request.args.get('proposalID')
        msg = updateProposal(proposalID, type)
        return redirect("/task/" + "123456")


@app.route("/new", methods=["GET"])
def new_task():
    task_form = TaskForm()
    return render_template("new.html", task_form=task_form)


@app.route("/new", methods=["POST"])
def new_task_post():
    task_form = TaskForm(request.form)
    title = request.form
    if task_form.validate():
        title = request.form["title"]
        location = request.form["location"]
        price = float(request.form["price"])
        description = request.form["description"]
        user = 123456 #TODO: change user ID
        try:
            task = Tasks(title = title,
                location = location,
                price = price,
                description = description,
                user = user,
                type = "T1")
            db.session.add(task)
            db.session.commit()
            link = "/task/{}".format(task.id)
            return redirect(link)
        except Exception as e:
            return render_template("new.html", task_form=task_form)
    else:
        return render_template("new.html", task_form=task_form)



if __name__ == '__main__':
    app.run(debug=True)
