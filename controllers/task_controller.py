from app import db
from models import Tasks

def get_all_tasks():
    tasks = Tasks.query.order_by(Tasks.created_at).all()
    return tasks

def get_task(id):
    task = Task.query.get(id)
    return task
