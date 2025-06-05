from typing import Sequence

from backend.src.modules.applications.repository import ApplicationRepository
from backend.src.modules.applications.schemas import AppAddForm, ApplicationSchema
from backend.src.modules.users.schemas import UserSchema


class ApplicationService:

    def __init__(self, application_repo: ApplicationRepository):
        self.application_repo = application_repo

    async def add(self, add_form: AppAddForm, user: UserSchema) -> ApplicationSchema:
        app = await self.application_repo.add(
            user_id=user.id,
            service=add_form.service,
            description=add_form.description
        )
        schema = ApplicationSchema.model_validate(app)
        return schema

    async def get_all(self, **kwargs) -> Sequence[ApplicationSchema]:
        apps = await self.application_repo.get_all(**kwargs)
        return [ApplicationSchema.model_validate(app) for app in apps]
