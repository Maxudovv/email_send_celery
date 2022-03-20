from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
import re

from app.tasks import send_email


class SendEmailView(APIView):
    email_regexp = r"\w+@\w+\.\w+"

    def post(self, request, *args, **kwargs):
        email = request.data.get("email")
        if email is None or not isinstance(email, str):
            return Response(
                data={"error": "Email field is required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        validated_email = re.search(self.email_regexp, email)
        if validated_email is None:
            return Response(
                data={"error": "Not valid email"}, status=status.HTTP_400_BAD_REQUEST
            )

        send_email.delay(email)

        return Response(data={"isSent": True}, status=status.HTTP_200_OK)
