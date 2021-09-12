from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework import status

from .serializers import RegisterSerializer, LoginSerializer


class RegisterApi(APIView):
    permission_classes = (AllowAny,)

    def post(self, request):
        if request.user.is_authenticated:
            raise ValidationError("Only new users can signup")
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)
