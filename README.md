# task-task-service-app

# Task Service (FastAPI)

## Features
- Create Task
- Get Task
- Get Tasks by User
- Update Task Status
- Validates user via User Service

## Tech Stack
- FastAPI
- Docker
- Kubernetes (separate repo)

## Run locally

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload