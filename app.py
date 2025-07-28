from flask import Flask, request, jsonify
from app.models import db, Task


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///tasks.db"
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{"id": t.id, "description": t.description} for t in tasks])

@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    new_task = Task(description=data["description"])
    db.session.add(new_task)
    db.session.commit()
    return jsonify({"message": "Task created"}), 201

@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    task = Task.query.get_or_404(task_id)
    db.session.delete(task)
    db.session.commit()
    return jsonify({"message": "Task deleted"})

@app.route("/")
def home():
    return {"message": "Task Manager API is running"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

