from rest_framework import serializers

from . import models


class DocumentSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Document
        fields = [
            "id",
            "created",
            "last_updated",
            "uploaded_at",
            "file",
            "project",
        ]

class ResearchProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.ResearchProject
        fields = [
            "created",
            "end_date",
            "title",
            "description",
            "last_updated",
            "id",
            "start_date",
            "lead",
        ]

class TeamSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Team
        fields = [
            "id",
            "last_updated",
            "created",
            "role",
            "project",
            "member",
        ]
