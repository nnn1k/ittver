from fastapi import APIRouter, Depends

from backend.src.mail import SendEmail
from backend.src.modules.users.schemas import MessageForm

router = APIRouter(
    prefix="/startpage",
    tags=["startpage"],
)


@router.post('/mail')
async def send_mail(
    msg_form: MessageForm,
):
    message = f"""
        Имя: {msg_form.name}
        Номер: {msg_form.phone}
        Сообщение: {msg_form.message}
    """
    await SendEmail.post_mail(user_to=msg_form.email_to, message=message)
    return {'msg': 'Сообщение отправлено'}


