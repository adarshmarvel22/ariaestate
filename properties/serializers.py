from rest_framework import serializers

from . import models


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Category
        fields = [
            "created",
            "id",
            "last_updated",
            "description",
            "name",
        ]

class LeaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Lease
        fields = [
            "monthly_rent",
            "start_date",
            "tenant_name",
            "end_date",
            "created",
            "id",
            "last_updated",
            "unit",
        ]

class ProjectSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Project
        fields = [
            "last_updated",
            "launch_date",
            "price_range",
            "title",
            "description",
            "created",
            "id",
            "location",
            "category",
        ]

class UnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Unit
        fields = [
            "created",
            "last_updated",
            "id",
            "size_sqft",
            "unit_number",
            "is_available",
            "price",
            "project",
        ]
