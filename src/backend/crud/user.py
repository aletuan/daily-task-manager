from sqlalchemy.orm import Session
from typing import Optional

from ..models.user import User
from ..schemas.user import UserCreate


class UserCRUD:
    def create(self, db: Session, user_data: UserCreate) -> User:
        """Create a new user"""
        # TODO: Implement password hashing
        db_user = User(
            email=user_data.email,
            username=user_data.username,
            hashed_password=user_data.password  # TODO: Hash password
        )
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    
    def get_by_id(self, db: Session, user_id: int) -> Optional[User]:
        """Get user by ID"""
        return db.query(User).filter(User.id == user_id).first()
    
    def get_by_email(self, db: Session, email: str) -> Optional[User]:
        """Get user by email"""
        return db.query(User).filter(User.email == email).first()


# Create instance
user_crud = UserCRUD() 