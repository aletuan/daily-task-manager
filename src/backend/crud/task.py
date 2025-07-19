from sqlalchemy.orm import Session
from sqlalchemy import and_, or_, desc, asc
from typing import List, Optional
from datetime import datetime

from ..models.task import Task, StatusEnum
from ..schemas.task import TaskCreate, TaskUpdate


class TaskCRUD:
    def create(self, db: Session, task_data: TaskCreate, user_id: int) -> Task:
        """Create a new task for a user"""
        db_task = Task(
            **task_data.dict(),
            user_id=user_id
        )
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task
    
    def get_by_id(self, db: Session, task_id: int, user_id: int) -> Optional[Task]:
        """Get a specific task by ID for a user"""
        return db.query(Task).filter(
            and_(Task.id == task_id, Task.user_id == user_id)
        ).first()
    
    def get_all(
        self, 
        db: Session, 
        user_id: int, 
        skip: int = 0, 
        limit: int = 100,
        status: Optional[StatusEnum] = None,
        priority: Optional[str] = None,
        category_id: Optional[int] = None
    ) -> List[Task]:
        """Get all tasks for a user with optional filtering"""
        query = db.query(Task).filter(Task.user_id == user_id)
        
        if status:
            query = query.filter(Task.status == status)
        if priority:
            query = query.filter(Task.priority == priority)
        if category_id:
            query = query.filter(Task.category_id == category_id)
        
        return query.offset(skip).limit(limit).all()
    
    def update(self, db: Session, task_id: int, user_id: int, task_data: TaskUpdate) -> Optional[Task]:
        """Update a task"""
        db_task = self.get_by_id(db, task_id, user_id)
        if not db_task:
            return None
        
        update_data = task_data.dict(exclude_unset=True)
        
        # Handle completion status
        if task_data.is_completed is not None:
            if task_data.is_completed and not db_task.is_completed:
                db_task.completed_at = datetime.utcnow()
                db_task.status = StatusEnum.DONE
            elif not task_data.is_completed:
                db_task.completed_at = None
        
        for field, value in update_data.items():
            setattr(db_task, field, value)
        
        db.commit()
        db.refresh(db_task)
        return db_task
    
    def delete(self, db: Session, task_id: int, user_id: int) -> bool:
        """Delete a task"""
        db_task = self.get_by_id(db, task_id, user_id)
        if not db_task:
            return False
        
        db.delete(db_task)
        db.commit()
        return True
    
    def mark_completed(self, db: Session, task_id: int, user_id: int) -> Optional[Task]:
        """Mark a task as completed"""
        db_task = self.get_by_id(db, task_id, user_id)
        if not db_task:
            return None
        
        db_task.is_completed = True
        db_task.status = StatusEnum.DONE
        db_task.completed_at = datetime.utcnow()
        
        db.commit()
        db.refresh(db_task)
        return db_task
    
    def get_by_status(self, db: Session, user_id: int, status: StatusEnum) -> List[Task]:
        """Get tasks by status for a user"""
        return db.query(Task).filter(
            and_(Task.user_id == user_id, Task.status == status)
        ).all()


# Create instance
task_crud = TaskCRUD() 