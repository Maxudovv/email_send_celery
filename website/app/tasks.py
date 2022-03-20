import smtplib
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from celery import shared_task
from django.conf import settings


@shared_task
def send_email(email):

    message = "SUCCESS"
    msg = MIMEMultipart()
    password = settings.EMAIL_PASSWORD
    msg["From"] = settings.EMAIL_NAME
    print(settings.EMAIL_NAME)
    msg["To"] = email
    msg["Subject"] = "Tripix"
    msg.attach(MIMEText(message, "plain"))
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
    except smtplib.SMTPServerDisconnected:
        return False
    server.starttls()
    server.login(msg["From"], password)
    server.sendmail(msg["From"], msg["To"], msg.as_string())
    server.quit()

    return True
