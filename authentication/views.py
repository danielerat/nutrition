import datetime
import random
import string
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import exceptions
from authentication.authentication import JWTAuthentication, create_access_token, create_refresh_token, decode_access_token, decode_refresh_token

from authentication.serializers import UserSerializer
from authentication.models import Reset, User, UserToken


class RegisterAPIView(APIView):
    authentication_classes = []

    def post(self, request):
        data = request.data
        if data['password'] != data['password_confirm']:
            raise exceptions.APIException("Password Do Not Match")
        serializer = UserSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class LoginAPIView(APIView):
    authentication_classes = []

    def post(self, request):
        phone_number = request.data['phone_number']
        password = request.data['password']

        user = User.objects.filter(phone_number=phone_number).first()
        if user is None:
            raise exceptions.AuthenticationFailed("Invalid Credentials")

        if not user.check_password(password):
            raise exceptions.AuthenticationFailed("Invalid Credentials")

        # reate an access Token
        access_token = create_access_token(user.id)
        refresh_token = create_refresh_token(user.id)

        # Store in the user token db
        UserToken.objects.create(
            user_id=user.id,
            token=refresh_token,
            expired_at=datetime.datetime.utcnow() + datetime.timedelta(days=7)
        )

        response = Response()
        response.set_cookie(key='refresh_token',
                            value=refresh_token, httponly=True)
        response.data = {
            'token': access_token
        }

        return response
