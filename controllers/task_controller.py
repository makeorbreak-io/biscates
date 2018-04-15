from app import db
from models import Tasks
from models import Users
from models import Proposals
from flask import jsonify
from models import Ratings, Type


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


def get_user_by_email(email):
    return Users.query.filter_by(email=email).first()


def validate_login(email, password):
    user = Users.query.filter_by(email=email).first()
    if user and user.email == email and user.password == password:
        return user.id
    return None


def register_user(email, name, password):
    user = Users(name, email, password)

    try:
        db.session.add(user)
        db.session.commit()
    except Exception:
        db.session.rollback()
        return False

    return user.id

def get_proposals(task_id):
    proposals = Proposals.query.filter_by(task=task_id).all()
    return proposals

def update_proposal(proposalID, type):

    proposal = Proposals.query.filter_by(id=proposalID).first()

    print ("update Proposal")
    print(proposalID)

    status = 200
    msg = "Proposta aceite"

    if proposal is not None:

     if type == 'accept':
        proposal.accepted = True
        print(proposal)
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

    print(proposal)

    try:

        db.session.add(proposal)
        db.session.commit()
        return jsonify({"status": 203, "msg": "Proposta guardada"})

    except Exception as  e:
        print(e)
        db.session.rollback()
        return jsonify({"status": 400, "msg": "Erro ao guardar proposta"})


def get_task_types():
    types = []
    for type in Type.__members__:
        types.append(type)
    return types
