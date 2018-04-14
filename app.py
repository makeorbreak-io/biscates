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
    return render_template("homepage.html", tasks=tasks)


@app.route("/task")
def taks():
    return render_template("task.html")


@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/proposal", methods=['POST'])
def offer():
       if request.method == 'POST':

            type = request.args.get('type')

            if type == 'create':

                user = request.args.get('user')
                offer = request.args.get('offer')
                description = request.args.get('description')
                insertProposal(taskID, user, offer, description)

            else:

                proposalID = request.args.get('proposalID')
                response = updateProposal(proposalID, type)



if __name__ == '__main__':
    app.run(debug=True)
