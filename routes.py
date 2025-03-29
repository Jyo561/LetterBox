from fastapi import APIRouter
from controllers import store_controller, auth_controller, drive_controller
from dotenv import load_dotenv
import os
from fastapi.responses import JSONResponse

load_dotenv()
router = APIRouter()

# Include API controllers
router.include_router(auth_controller.router, prefix="/auth", tags=["auth"])
router.include_router(drive_controller.router, prefix="/drive", tags=["drive"])
router.include_router(store_controller.router, prefix="/store", tags=["Store"])
