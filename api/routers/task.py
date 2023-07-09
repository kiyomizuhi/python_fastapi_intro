from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from api.schemas import Task, TaskCreate, TaskCreateResponse
from api.cruds import get_tasks_with_done, create_task, get_task 
from api.db import get_db

router = APIRouter()


@router.get("/tasks", response_model=list[Task])
async def list_tasks(
    db: AsyncSession = Depends(get_db)
):
    return await get_tasks_with_done(db)


@router.post("/tasks", response_model=TaskCreateResponse)
async def create_task(
    task_body: TaskCreate,
    db: AsyncSession = Depends(get_db),
):
    return await create_task(db, task_body)


@router.put("/tasks/{task_id}", response_model=TaskCreateResponse)
async def update_task(
    task_id: int,
    task_body: TaskCreate,
    db: AsyncSession,
):
    task = await get_task(db, task_id=task_id)
