from app import db

from models import Proposals


def updateProposal(proposalID, type):
    proposal = Proposals.query.filter_by(id=proposalID).first()

    status = 200
    msg = "Proposta aceite"

    if not proposal.isNull()
    if type == 'accept'
       proposal.accepted = True
    elif  type == 'reject'
       proposal.accepted = False
    else
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