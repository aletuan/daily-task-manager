from sqlalchemy import Column, Integer, String, Text, DateTime, Enum, ForeignKey, Boolean
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
import enum
from .base import Base


class PriorityEnum(enum.Enum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class StatusEnum(enum.Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


class Task(Base):
    __tablename__ = "tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    priority = Column(Enum(PriorityEnum), default=PriorityEnum.MEDIUM)
    status = Column(Enum(StatusEnum), default=StatusEnum.TODO)
    due_date = Column(DateTime(timezone=True), nullable=True)
    is_completed = Column(Boolean, default=False)
    completed_at = Column(DateTime(timezone=True), nullable=True)
    
    # Foreign Keys
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=True)
    
    # Timestamps
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
    
    # Relationships
    user = relationship("User", back_populates="tasks")
    category = relationship("Category", back_populates="tasks") 