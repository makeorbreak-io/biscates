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

def get_task(id):
    task = Tasks.query.get(id)
    return task



def updateProposal(proposalID, type):
    proposal = Proposals.query.filter_by(id=proposalID).first()

    status = 200
    msg = "Proposta aceite"

    if proposal is not None:

     if type is 'accept':

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

    proposal = Proposals(user, offer, description, taskID)

    try:

        db.session.add(proposal)
        db.session.commit()
        return jsonify({"status": 203, "msg": "Proposta guardada"})

    except:

        db.session.rollback()
        return jsonify({"status": 400, "msg": "Erro ao guardar proposta"})