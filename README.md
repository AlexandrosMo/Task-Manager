# Task Manager API

Simple REST API to manage tasks. Built with Flask + SQLite.

## Endpoints

- `GET /tasks` – List all tasks  
- `POST /tasks` – Create a new task (JSON: `{ "description": "My task" }`)  
- `DELETE /tasks/<id>` – Delete a task by ID  
