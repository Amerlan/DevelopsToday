from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=80, unique=True)
    link = models.SlugField(max_length=60, editable=False)
    created_at = models.DateTimeField(auto_now=True, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    upvotes = models.ManyToManyField(User, related_name='upvotes', blank=True)

    @property
    def upvote_count(self):
        return self.upvotes.count()

    @property
    def author_name(self):
        return self.author.username

    @property
    def created_at_pretty(self):
        return f"{self.created_at.astimezone()}".split('.')[0]


class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    post = models.ForeignKey('posts.Post', on_delete=models.CASCADE, blank=True)
    content = models.TextField(max_length=500, default="")
    created_at = models.DateTimeField(auto_now=True, editable=False)
