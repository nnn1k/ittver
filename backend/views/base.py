from fastapi import APIRouter

from backend.views.test import router as test_router

backend_router = APIRouter(
    prefix='/api'
)

backend_router.include_router(test_router)
