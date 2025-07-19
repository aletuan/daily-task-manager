from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from typing import List, Optional

from ..database.session import get_db
from ..crud.task import task_crud
from ..schemas.task import TaskCreate, TaskUpdate, TaskResponse, TaskList
from ..models.task import StatusEnum

router = APIRouter(prefix="/tasks", tags=["tasks"])


@router.post("/", response_model=TaskResponse, status_code=status.HTTP_201_CREATED)
async def create_task(
    task_data: TaskCreate,
    db: Session = Depends(get_db),
    user_id: int = 1  # TODO: Replace with actual user authentication
):
    """
    Create a new task for the authenticated user.
    
    - **title**: Task title (required)
    - **description**: Task description (optional)
    - **priority**: Task priority (low, medium, high)
    - **due_date**: Task due date (optional)
    - **category_id**: Category ID for organization (optional)
    """
    try:
        task = task_crud.create(db=db, task_data=task_data, user_id=user_id)
        return task
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Failed to create task: {str(e)}"
        )


@router.get("/", response_model=TaskList)
async def get_tasks(
    skip: int = Query(0, ge=0, description="Number of tasks to skip"),
    limit: int = Query(100, ge=1, le=1000, description="Number of tasks to return"),
    status: Optional[StatusEnum] = Query(None, description="Filter by task status"),
    priority: Optional[str] = Query(None, description="Filter by task priority"),
    category_id: Optional[int] = Query(None, description="Filter by category ID"),
    db: Session = Depends(get_db),
    user_id: int = 1  # TODO: Replace with actual user authentication
):
    """
    Get all tasks for the authenticated user with optional filtering.
    
    - **skip**: Number of tasks to skip for pagination
    - **limit**: Maximum number of tasks to return
    - **status**: Filter by task status (todo, in_progress, done)
    - **priority**: Filter by priority (low, medium, high)
    - **category_id**: Filter by category ID
    """
    tasks = task_crud.get_all(
        db=db,
        user_id=user_id,
        skip=skip,
        limit=limit,
        status=status,
        priority=priority,
        category_id=category_id
    )
    
    total = len(tasks)  # TODO: Implement proper count query
    
    return TaskList(
        tasks=tasks,
        total=total,
        page=skip // limit + 1,
        size=limit
    )


@router.get("/{task_id}", response_model=TaskResponse)
async def get_task(
    task_id: int,
    db: Session = Depends(get_db),
    user_id: int = 1  # TODO: Replace with actual user authentication
):
    """
    Get a specific task by ID.
    """
    task = task_crud.get_by_id(db=db, task_id=task_id, user_id=user_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    return task


@router.put("/{task_id}", response_model=TaskResponse)
async def update_task(
    task_id: int,
    task_data: TaskUpdate,
    db: Session = Depends(get_db),
    user_id: int = 1  # TODO: Replace with actual user authentication
):
    """
    Update a specific task.
    """
    task = task_crud.update(db=db, task_id=task_id, user_id=user_id, task_data=task_data)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    return task


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    user_id: int = 1  # TODO: Replace with actual user authentication
):
    """
    Delete a specific task.
    """
    success = task_crud.delete(db=db, task_id=task_id, user_id=user_id)
    if not success:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )


@router.patch("/{task_id}/complete", response_model=TaskResponse)
async def mark_task_completed(
    task_id: int,
    db: Session = Depends(get_db),
    user_id: int = 1  # TODO: Replace with actual user authentication
):
    """
    Mark a task as completed.
    """
    task = task_crud.mark_completed(db=db, task_id=task_id, user_id=user_id)
    if not task:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Task not found"
        )
    return task


@router.get("/status/{status}", response_model=List[TaskResponse])
async def get_tasks_by_status(
    status: StatusEnum,
    db: Session = Depends(get_db),
    user_id: int = 1  # TODO: Replace with actual user authentication
):
    """
    Get all tasks for a specific status.
    """
    tasks = task_crud.get_by_status(db=db, user_id=user_id, status=status)
    return tasks 