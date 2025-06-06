import string
import random

from aiosmtplib import SMTP

from backend.src.settings import settings


class SendEmail:

    @staticmethod
    async def post_mail(user_to, message) -> None:
        smt = SMTP(hostname='smtp.gmail.com', port=587, start_tls=True)
        await smt.connect()
        await smt.login(settings.email.login, settings.email.password)
        await smt.sendmail(settings.email.login, user_to, message.encode('utf-8'))
        await smt.quit()

