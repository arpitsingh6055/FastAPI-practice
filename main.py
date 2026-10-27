import asyncio
from dataclasses import dataclass
from fastapi import FastAPI
from pydantic import BaseModel

class Project(BaseModel):
    id: int
    name: str
    description: str

class Deadline():
    project_id: int
    deadline: str



# This is the variable name FastAPI looks for by default
app = FastAPI(title="My FastAPI Application", description="This is a sample FastAPI application.", version="1.0.0")

@app.get("/")
def read_root():
    return {"status": "success", "message": "FastAPI is working!"}


@app.get("/projects/{project_id}")
async def get_project(project_id: int) -> Project | dict:
    project = mock_database_query(project_id)
    if project:
        return project
    else:
        return {"error": "Project not found"}

@app.get("/names")
async def get_item_names():
    await asyncio.sleep(5)
    return {"items": ["item1", "item2", "item3"]}  # Simulate a delay for demonstration purposes


def mock_database_query(project_id : int)-> Project | None:
    projects = {
        "project1" : Project(id=1, name="Project 1", description="This is project 1"),
        "project2" : Project(id=2, name="Project 2", description="This is project 2"),
        "project3" : Project(id=3, name="Project 3", description="This is project 3"),
        "project4" : Project(id=4, name="Project 4", description="This is project 4"),
    }
    return projects[f"project{project_id}"] if f"project{project_id}" in projects else None