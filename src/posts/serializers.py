from rest_framework import serializers
from django.utils.text import slugify

from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        read_only_fields = (
            "created_at_pretty",
            "upvote_count",
            "link",
            "author_name",
        )
        fields = read_only_fields + ("title",)

    def validate(self, data):
        request = self.context.get("request")
        user = request.user
        data["author"] = user
        data["link"] = slugify(data.get("title", ""))
        return data


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

    def validate(self, data):
        request = self.context.get("request")
        post = self.context.get("post")
        user = request.user
        data["author"] = user
        data["post"] = post
        return data
