from sqlalchemy.orm import Session
from typing import List, Optional

from ..models.category import Category
from ..schemas.category import CategoryCreate


class CategoryCRUD:
    def create(self, db: Session, category_data: CategoryCreate, user_id: int) -> Category:
        """Create a new category for a user"""
        db_category = Category(
            **category_data.dict(),
            user_id=user_id
        )
        db.add(db_category)
        db.commit()
        db.refresh(db_category)
        return db_category
    
    def get_by_id(self, db: Session, category_id: int, user_id: int) -> Optional[Category]:
        """Get category by ID for a user"""
        return db.query(Category).filter(
            Category.id == category_id,
            Category.user_id == user_id
        ).first()
    
    def get_all(self, db: Session, user_id: int) -> List[Category]:
        """Get all categories for a user"""
        return db.query(Category).filter(Category.user_id == user_id).all()


# Create instance
category_crud = CategoryCRUD() 