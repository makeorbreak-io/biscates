from app import db
from models import Tasks
from models import Users


def get_all_tasks():
    tasks = Tasks.query.filter_by(approved=False).order_by(Tasks.created_at).limit(10).all()
    return tasks

def get_user_by_id(id):
    user = Users.query.get(id)
    return user

def get_task(id):
    task = Tasks.query.get(id)
    return task
