from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
from .models import Post, Comment
from .serializers import PostSerializer


class PostViewSet(ViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = Post.objects.all()
    serializer = PostSerializer

    def list(self, request):
        serializer = self.serializer(self.queryset, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def retrieve(self, request, link):
        post = get_object_or_404(self.queryset, link=link)
        serializer = self.serializer(post)
        return Response(status=status.HTTP_200_OK, data=serializer.data)
