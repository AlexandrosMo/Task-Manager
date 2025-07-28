from flask import Blueprint, request, jsonify
from .models import db, Task

main = Blueprint('main', __name__)

@main.route("/")
def home():
    return {"message": "Task Manager API is running"}

@main.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{"id": t.id, "description": t.description} for t in tasks])

@main.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    new_task = Task(description=data["description"])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task created"}), 201

@main.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"})
