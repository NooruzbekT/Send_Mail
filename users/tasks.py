from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_email_task(subject, message, recipient_list):
    send_mail(
        subject=subject,
        message="",
        from_email="your_email@gmail.com",
        recipient_list=recipient_list,
        html_message=message
    )
