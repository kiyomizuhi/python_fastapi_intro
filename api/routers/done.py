from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.schemas import DoneResponse
from api.cruds import get_done, create_done, delete_done
from api.db import get_db

router = APIRouter()

@router.put("/tasks/{task_id}/done", response_model=DoneResponse)
async def mark_task_as_done(
    task_id: int,
    db: AsyncSession = Depends(get_db),
):
    done = await get_done(db, task_id=task_id)
    if done is not None:
        raise HTTPException(
            status_code=400,
            detail="Done already exists"
        )
    return await create_done(db, task_id)


@router.delete("/tasks/{task_id}/done", response_model=None)
async def unmark_task_as_done(
    task_id: int,
    db: AsyncSession = Depends(get_db),
):
    done = await get_done(db, task_id=task_id)
    if done is None:
        raise HTTPException(
            status_code=404,
            detail="Done not found"
        )
    return await delete_done(db, original=done)
