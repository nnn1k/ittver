from fastapi import APIRouter

from backend.views.test import router as test_router
from backend.views.auth import router as auth_router
from backend.views.users import router as users_router
from backend.views.applications import router as applications_router
from backend.views.startpage import router as startpage_router
from backend.views.reviews import router as reviews_router

backend_router = APIRouter(
    prefix='/api'
)

backend_router.include_router(test_router)

backend_router.include_router(auth_router)
backend_router.include_router(users_router)
backend_router.include_router(applications_router)
backend_router.include_router(startpage_router)
backend_router.include_router(reviews_router)
