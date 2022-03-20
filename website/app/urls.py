from django.urls import path

from app.views import SendEmailView

urlpatterns = [
    path("send_email/", SendEmailView.as_view())
]
