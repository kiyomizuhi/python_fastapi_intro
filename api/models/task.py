from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

from api.db import Base


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, ForeignKey="task_id", primary_key=True)
    title = Column(String(1024))
    due_date = Column(Date)

    done = relationship("Done", back_populates="task", cascade="delete")
