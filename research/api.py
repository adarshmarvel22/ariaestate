from rest_framework import viewsets, permissions

from . import serializers
from . import models


class DocumentViewSet(viewsets.ModelViewSet):
    """ViewSet for the Document class"""

    queryset = models.Document.objects.all()
    serializer_class = serializers.DocumentSerializer
    permission_classes = [permissions.IsAuthenticated]


class ResearchProjectViewSet(viewsets.ModelViewSet):
    """ViewSet for the ResearchProject class"""

    queryset = models.ResearchProject.objects.all()
    serializer_class = serializers.ResearchProjectSerializer
    permission_classes = [permissions.IsAuthenticated]


class TeamViewSet(viewsets.ModelViewSet):
    """ViewSet for the Team class"""

    queryset = models.Team.objects.all()
    serializer_class = serializers.TeamSerializer
    permission_classes = [permissions.IsAuthenticated]
