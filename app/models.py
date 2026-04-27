from pydantic import BaseModel

class Task(BaseModel):
    title: str
    description: str
    userId: str

class TaskStatusUpdate(BaseModel):
    status: str