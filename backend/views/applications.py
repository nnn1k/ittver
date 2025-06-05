from fastapi import APIRouter, Depends

from backend.src.modules.applications.dependencies import get_app_serv
from backend.src.modules.applications.schemas import AppAddForm
from backend.src.modules.applications.service import ApplicationService
from backend.src.modules.auth.dependencies import get_user_by_token
from backend.src.modules.users.schemas import UserSchema

router = APIRouter(
    prefix="/applications",
    tags=["applications"],
)


@router.get("/me")
async def get_my_app(
        user: UserSchema = Depends(get_user_by_token),
        service: ApplicationService = Depends(get_app_serv)
):
    apps = await service.get_all(user_id=user.id)
    return {"applications": apps}


@router.post("")
async def create_new_application(
        add_form: AppAddForm,
        user: UserSchema = Depends(get_user_by_token),
        service: ApplicationService = Depends(get_app_serv)
):
    app = await service.add(add_form=add_form, user=user)
    return {"applications": app}
