from fastapi import FastAPI, HTTPException
from app.models import Task, TaskStatusUpdate
from app.store import tasks
from app.user_client import get_user

app = FastAPI()


# -------------------------
# CREATE TASK
# -------------------------
@app.post("/tasks")
def create_task(task: Task):

    user = get_user(task.userId)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    task_id = str(len(tasks) + 1)

    new_task = Task(
        id=task_id,
        title=task.title,
        description=task.description,
        userId=task.userId,
        status="TODO"
    )

    tasks[task_id] = new_task

    return new_task


# -------------------------
# GET TASK
# -------------------------
@app.get("/tasks/{task_id}")
def get_task(task_id: str):

    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    return tasks[task_id]


# -------------------------
# GET TASKS BY USER
# -------------------------
@app.get("/tasks/user/{user_id}")
def get_tasks_by_user(user_id: str):

    return [
        t for t in tasks.values()
        if t.userId == user_id
    ]


# -------------------------
# UPDATE TASK STATUS
# -------------------------
@app.patch("/tasks/{task_id}")
def update_task(task_id: str, body: TaskStatusUpdate):

    if task_id not in tasks:
        raise HTTPException(status_code=404, detail="Task not found")

    task = tasks[task_id]

    task.status = body.status

    return task