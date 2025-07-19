from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])


@router.get("/me")
async def get_current_user():
    """
    Get current user information.
    TODO: Implement authentication
    """
    return {"message": "Authentication not implemented yet"} 