from rest_framework import serializers
from django.utils.text import slugify

from .models import Post, Comment


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        read_only_fields = (
            'created_at_pretty', 'upvotes', 'upvote_count',
            'link', 'author_name',
        )
        fields = read_only_fields + ('title', )

    def create(self, validated_data):
        request = self.context.get("request")
        user = request.user
        validated_data['link'] = slugify(validated_data.get('title', ''))
        post = Post(author=user, **validated_data)
        post.save()
        return post


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'



