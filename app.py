import os
from flask import Flask, render_template, jsonify, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField,TextField, PasswordField
from wtforms.validators import DataRequired, Email, EqualTo
from wtforms.fields.html5 import EmailField
from controllers.task_controller import *
from flask_login import LoginManager



app = Flask(__name__)
app.secret_key = os.environ['SECRET_KEY']
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


class LoginForm(FlaskForm):
    email = EmailField('Email', [DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])

class NewProposalForm(FlaskForm):
    user = StringField('Utilizador', [DataRequired()])
    offer = StringField('Preço', [DataRequired()])
    description = TextField('Descrição', [DataRequired()])
    task_id = StringField('task_id',[DataRequired()])
    type = StringField('type', [DataRequired()])


class RegisterForm(FlaskForm):
    email = EmailField('Email', [DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirmar Password', validators=[
        DataRequired(),
        EqualTo('password', message='Passwords devem ser idênticas')
    ])


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


@app.route("/task")
def taks():
    newproposal_form = NewProposalForm()
    task_id = request.args.get('id')
    task = get_task(task_id)
    task.user_info = get_user_by_id(task.user)
    return render_template("task.html", task=task, newproposal_form=newproposal_form)


@app.route("/profile")
def profile():
    user_id = request.args.get('id')
    user = get_user_by_id(user_id)
    tasks = get_user_tasks(user_id)
    for task in tasks:
        task.rating = get_task_rating(task.id)
    return render_template("profile.html", user=user, tasks=tasks)


@app.route("/proposal", methods=['POST'])
def offer():
            type = request.args.get('type')
            print(request.args)



            if type is 'create':
                taskID = request.args.get(task_id)
                user = request.args.get('user')
                offer = request.args.get('offer')
                description = request.args.get('description')
                msg = insertProposal(taskID, user, offer, description)
                print("lol")
                taskID = "/task?id=" + taskID
                return redirect(taskID)

            else:
                print("benfas")
                print(type)
                proposalID = request.args.get('proposalID')
                msg = updateProposal(proposalID, type)
                return redirect("/task?id=" + "123456")




if __name__ == '__main__':
    app.run(debug=True)
