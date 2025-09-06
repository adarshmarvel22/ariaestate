from django.contrib import admin
from django import forms

from . import models


class DocumentAdminForm(forms.ModelForm):

    class Meta:
        model = models.Document
        fields = "__all__"


class DocumentAdmin(admin.ModelAdmin):
    form = DocumentAdminForm
    list_display = [
        "id",
        "created",
        "last_updated",
        "uploaded_at",
        "file",
    ]
    readonly_fields = [
        "id",
        "created",
        "last_updated",
        "uploaded_at",
        "file",
    ]


class ResearchProjectAdminForm(forms.ModelForm):

    class Meta:
        model = models.ResearchProject
        fields = "__all__"


class ResearchProjectAdmin(admin.ModelAdmin):
    form = ResearchProjectAdminForm
    list_display = [
        "created",
        "end_date",
        "title",
        "description",
        "last_updated",
        "id",
        "start_date",
    ]
    readonly_fields = [
        "created",
        "end_date",
        "title",
        "description",
        "last_updated",
        "id",
        "start_date",
    ]


class TeamAdminForm(forms.ModelForm):

    class Meta:
        model = models.Team
        fields = "__all__"


class TeamAdmin(admin.ModelAdmin):
    form = TeamAdminForm
    list_display = [
        "id",
        "last_updated",
        "created",
        "role",
    ]
    readonly_fields = [
        "id",
        "last_updated",
        "created",
        "role",
    ]


admin.site.register(models.Document, DocumentAdmin)
admin.site.register(models.ResearchProject, ResearchProjectAdmin)
admin.site.register(models.Team, TeamAdmin)
