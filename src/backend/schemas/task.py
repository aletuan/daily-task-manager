from pydantic import BaseModel, Field
from typing import Optional, List
from datetime import datetime
from enum import Enum


class PriorityEnum(str, Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class StatusEnum(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class TaskBase(BaseModel):
    title: str = Field(..., min_length=1, max_length=255, description="Task title")
    description: Optional[str] = Field(None, max_length=1000, description="Task description")
    priority: PriorityEnum = Field(PriorityEnum.MEDIUM, description="Task priority level")
    due_date: Optional[datetime] = Field(None, description="Task due date")
    category_id: Optional[int] = Field(None, description="Category ID for task organization")


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=255)
    description: Optional[str] = Field(None, max_length=1000)
    priority: Optional[PriorityEnum] = None
    status: Optional[StatusEnum] = None
    due_date: Optional[datetime] = None
    category_id: Optional[int] = None
    is_completed: Optional[bool] = None


class TaskResponse(TaskBase):
    id: int
    status: StatusEnum
    is_completed: bool
    completed_at: Optional[datetime]
    user_id: int
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True


class TaskList(BaseModel):
    tasks: List[TaskResponse]
    total: int
    page: int
    size: int 