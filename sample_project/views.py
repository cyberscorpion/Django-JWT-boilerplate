from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework import status
from .serializers import *

from user.serializers import UserDetailSerializer
class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = CustomJWTSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.object.get('user') or request.user
            user_serialized_data = UserDetailSerializer(user).data
            token = serializer.object.get('token')
            response_data = {
                'token': token,
                "profile_photo": user_serialized_data['profile_photo'],
                "username": user_serialized_data["username"],
                "email": user_serialized_data["email"],
                "name": user_serialized_data["name"],
                "platform": user_serialized_data["platform"],
                "phone": user_serialized_data["phone"]
            }
            response = Response(response_data, status=status.HTTP_200_OK)
            if api_settings.JWT_AUTH_COOKIE:
                expiration = (datetime.utcnow() +
                              api_settings.JWT_EXPIRATION_DELTA)
                response.set_cookie(api_settings.JWT_AUTH_COOKIE,
                                    response.data['token'],
                                    expires=expiration,
                                    httponly=True)
            return response

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)