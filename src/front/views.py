from django.db.models import Count
from django.shortcuts import redirect, get_object_or_404
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from posts.models import Post
from posts.serializers import PostSerializer

# TODO: проверить все страницы. Сверстать их все
class BaseFrontApi(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    permission_classes = (IsAuthenticated,)


class RegisterPageApi(BaseFrontApi):
    permission_classes = (AllowAny,)
    template_name = 'signup.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('posts/')
        return Response(status=status.HTTP_200_OK)


class LoginPageApi(BaseFrontApi):
    permission_classes = (AllowAny,)
    template_name = 'login.html'

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('posts/')
        return Response(status=status.HTTP_200_OK)


class PostsPageApi(BaseFrontApi):
    template_name = 'posts.html'

    def get(self, request):
        posts = Post.objects.annotate(upvote_count=Count('upvotes')).order_by('-upvote_count')
        serializer = PostSerializer(posts, many=True)
        return Response(status=status.HTTP_200_OK, data={'posts': serializer.data})


class PostDetailPageApi(BaseFrontApi):
    template_name = 'post_detail.html'

    def get(self, request, slug):
        posts = get_object_or_404(Post, link=slug)
        serializer = PostSerializer(posts, many=True)
        return Response(status=status.HTTP_200_OK, data={'posts': serializer.data})
