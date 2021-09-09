from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from .models import Post, Comment


# TODO: реализовать CRUD для постов и коментов. Сделать апишку для лайка поста
class PostModelViewSet(ModelViewSet):
    queryset = Post.objects.all()
