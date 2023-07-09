from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession

from api.models import Done, Task
from api.schemas import *


async def get_tasks_with_done(
    db: AsyncSession,
) -> list[tuple[int, str, bool]]:
    result: Result = await db.execute(
        select(
            Task.id,
            Task.title,
            Task.due_date,
            Done.id.isnot(None).label("done"),
        ).outerjoin(Done)
    )
    return result.all()


async def create_task(
    db: AsyncSession,
    task_create: TaskCreate,
) -> Task:
    task = Task(**task_create.dict())
    db.add(task)
    await db.commit()
    await db.refresh(task)
    return task


async def get_task(db: AsyncSession, task_id: int) -> Task | None:
    result: Result = await db.execute(
        select(Task).filter(Task.id == task_id)
    )
    return result.scalars().first()


async def update_task(
    db: AsyncSession,
    task_create: TaskCreate,
    original: Task,
) -> Task:
    original.title = task_create.title
    original.due_date = task_create.due_date
    db.add(original)
    await db.commit()
    await db.refresh(original)
    return original


async def delete_task(
    db: AsyncSession,
    original: Task,
) -> None:
    await db.delete(original)
    await db.commit()
