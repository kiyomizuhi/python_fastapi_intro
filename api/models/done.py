from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.orm import relationship

from api.db import Base


class Done(Base):
    __tablename__ = "dones"

    id = Column(Integer, ForeignKey="task_id", primary_key=True)
    task = relationship("Task", back_populates="done")
