from app import db
from models import Tasks
from models import Users


def get_all_tasks():
    tasks = Tasks.query.filter_by(approved=False).order_by(Tasks.created_at).all()
    return tasks

def get_user_by_id(id):
    user = Users.query.get(id)
    return user

def get_task(id):
    task = Task.query.get(id)
    return task
