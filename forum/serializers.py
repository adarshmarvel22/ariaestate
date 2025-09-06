from rest_framework import serializers

from . import models


class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Comment
        fields = [
            "created",
            "id",
            "content",
            "last_updated",
            "post",
            "author",
        ]

class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Like
        fields = [
            "id",
            "created",
            "last_updated",
            "post",
            "user",
        ]

class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Post
        fields = [
            "last_updated",
            "created",
            "id",
            "content",
            "author",
            "tags",
        ]

class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Tag
        fields = [
            "last_updated",
            "name",
            "id",
            "created",
        ]
