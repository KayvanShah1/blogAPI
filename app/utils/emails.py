from fastapi import BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

from app.core import settings


email_config = ConnectionConfig(
    MAIL_USERNAME=settings.SMTP_USER,
    MAIL_PASSWORD=settings.SMTP_PASSWORD,
    MAIL_FROM=settings.EMAILS_FROM_EMAIL,
    MAIL_PORT=settings.SMTP_PORT,
    MAIL_SERVER=settings.SMTP_HOST,
    MAIL_FROM_NAME=settings.EMAILS_FROM_NAME,
    MAIL_TLS=settings.SMTP_TLS,
    MAIL_SSL=settings.SMTP_SSL,
    USE_CREDENTIALS=True,
    TEMPLATE_FOLDER=settings.EMAIL_TEMPLATES_DIR,
)


async def send_registration_mail(subject: str, email_to: str, body: dict):
    message = MessageSchema(
        subject=subject,
        recipients=[email_to],
        template_body=body,
        subtype="html",
    )

    fm = FastMail(email_config)
    await fm.send_message(message, template_name="registration_successful.html")
