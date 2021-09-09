from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=80)
    link = models.SlugField(max_length=60, default="", editable=False)
    created_at = models.DateTimeField(auto_created=True, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    upvotes = models.ManyToManyField(User, related_name='upvotes', through='PostLike')

    @property
    def upvote_count(self):
        return self.upvotes.count()

    @property
    def author_name(self):
        return self.author.username


class PostLike(models.Model):
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=500, default="")
    created_at = models.DateTimeField(auto_created=True, editable=False)
