import asyncio
import sys


def rebuild_schemas():
    from backend.src.modules.reviews.schemas import ReviewSchema
    from backend.src.modules.users.schemas import UserSchema, UserRelSchema
    from backend.src.modules.applications.schemas import ApplicationSchema
    ReviewSchema.model_rebuild()
    UserSchema.model_rebuild()
    ApplicationSchema.model_rebuild()
    UserRelSchema.model_rebuild()


