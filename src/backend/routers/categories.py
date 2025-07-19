from fastapi import APIRouter

router = APIRouter(prefix="/categories", tags=["categories"])


@router.get("/")
async def get_categories():
    """
    Get all categories for the current user.
    TODO: Implement category management
    """
    return {"message": "Category management not implemented yet"} 