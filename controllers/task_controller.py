from app import db
from models import Tasks
from models import Users
from models import Proposals
from flask import jsonify
from models import Ratings


def get_all_tasks():
    tasks = Tasks.query.filter_by(approved=False).order_by(Tasks.created_at).limit(10).all()
    return tasks

def get_user_by_id(id):
    user = Users.query.get(id)
    return user

def get_user_tasks(user_id):
    tasks = Tasks.query.filter_by(user=user_id).all()
    return tasks

def get_task_rating(id):
    rating = Ratings.query.filter_by(task=id).first()
    return rating

def get_task(id):
    task = Tasks.query.get(id)
    return task

def validate_login(email, password):
    user = Users.query.filter_by(email=email).first()
    if user and user.email == email and user.password == password:
        return user.id
    return None

def get_proposals(task_id):
    proposals = Proposals.query.filter_by(task=task_id).all()
    return proposals

def update_proposal(proposalID, type):

    proposal = Proposals.query.filter_by(id=proposalID).first()

    status = 200
    msg = "Proposta aceite"

    if proposal is not None:

     if type == 'accept':
        proposal.accepted = True
        db.session.commit()

     elif  type == 'reject':
        proposal.accepted = False
        db.session.commit()
     else:
        status = 400
        msg = "Erro ao alterar proposta"

    return jsonify({"status": status, "msg": msg})


def insertProposal(taskID, user, offer, description):

    proposal = Proposals(user, offer, description, False, taskID)

    try:

        db.session.add(proposal)
        db.session.commit()
        return jsonify({"status": 203, "msg": "Proposta guardada"})

    except Exception as  e:
        print(e)
        db.session.rollback()
        return jsonify({"status": 400, "msg": "Erro ao guardar proposta"})
