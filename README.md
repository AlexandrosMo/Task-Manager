# Task Manager API

A simple and lightweight RESTful API for managing tasks, built with Flask and SQLite.

## Overview

Task Manager API provides a straightforward way to create, list, and delete tasks. It is designed for simplicity and ease of use, ideal for small projects or as a learning tool for building RESTful APIs with Python Flask.

## Features

- List all tasks
- Create new tasks
- Delete tasks by ID
- Uses SQLite for persistent storage

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/AlexandrosMo/Task-Manager.git
   cd Task-Manager

    (Optional) Create and activate a Python virtual environment:

python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows

Install dependencies:

pip install -r requirements.txt

Run the Flask app:

    flask run

Usage

Once the application is running, you can interact with the API endpoints using tools like curl, Postman, or any HTTP client.
API Endpoints
Method	Endpoint	Description	Request Body
GET	/tasks	Retrieve all tasks	None
POST	/tasks	Create a new task	JSON: { "description": "Task description" }
DELETE	/tasks/<id>	Delete a task by its ID	None
Example

Create a new task:

curl -X POST http://localhost:5000/tasks -H "Content-Type: application/json" -d '{"description":"My first task"}'

Technologies

    Python 3.x

    Flask

    SQLite
