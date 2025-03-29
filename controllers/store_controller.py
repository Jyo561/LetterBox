from fastapi import APIRouter
#from services.user_service import get_all_users

router = APIRouter()


@router.get("/")
async def list_users():
    pass

