from rest_framework import serializers

from . import models


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Profile
        fields = [
            "avatar",
            "created",
            "last_updated",
            "phone",
            "bio",
            "id",
            "address",
            "user",
        ]

class RoleSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Role
        fields = [
            "id",
            "created",
            "last_updated",
            "name",
            "description",
        ]

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.User
        fields = [
            "id",
            "last_updated",
            "created",
            "role",
        ]
