from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings


@shared_task(name="send_feedback_email")
def send_feedback_email_task(email: str, subject: str, message: str):
    send_mail(
        subject=subject,
        message=message,
        from_email=settings.EMAIL_HOST_USER,
        recipient_list=[email],
        fail_silently=False,
    )
