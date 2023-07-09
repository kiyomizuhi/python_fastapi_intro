import datetime
from pydantic import BaseModel, Field

class TaskBase(BaseModel):
    title: str | None = Field(None, example="laundry")
    due_date: datetime.date | None = Field(None, example="2023-01-01")


class TaskCreate(TaskBase):
    pass


class TaskCreateResponse(TaskCreate):
    id: int

    class Config:
        orm_mode = True


class Task(TaskBase):
    id: int
    done: bool = Field(False, description="completed")

    class Config:
        orm_mode = True
