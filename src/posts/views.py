from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.viewsets import ViewSet
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer


class PostViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.annotate(count=Count("upvotes")).order_by("-count")
    serializer = PostSerializer

    def list(self, request):
        serializer = self.serializer(self.queryset, many=True)
        return Response(data=serializer.data)

    def retrieve(self, request, pk):
        post = get_object_or_404(self.queryset, link=pk)
        serializer = self.serializer(post)
        return Response(data=serializer.data)

    def create(self, request):
        serializer = self.serializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_201_CREATED)

    def partial_update(self, request, pk):
        post = get_object_or_404(self.queryset, link=pk)
        post.upvotes.add(request.user)
        return Response(status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        post = get_object_or_404(self.queryset, link=pk)
        if post.author != request.user:
            raise ValidationError("It's not your post")
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CommentViewSet(ViewSet):
    permission_classes = (IsAuthenticated,)
    serializer_class = CommentSerializer

    def list(self, request, post_pk):
        post = get_object_or_404(Post, link=post_pk)
        comments = Comment.objects.filter(post=post)
        serializer = self.serializer_class(comments, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk, post_pk):
        post = get_object_or_404(Post, link=post_pk)
        comment = get_object_or_404(Comment, post=post, pk=pk)
        serializer = self.serializer_class(comment)
        return Response(serializer.data)

    def create(self, request, post_pk):
        post = get_object_or_404(Post, link=post_pk)
        serializer = self.serializer_class(
            data=request.data, context={"request": request, "post": post}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def destroy(self, request, post_pk):
        post = get_object_or_404(Post, link=post_pk)
        if post.author != request.user:
            raise ValidationError("It's not your post")
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
