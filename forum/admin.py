from django.contrib import admin
from django import forms

from . import models


class CommentAdminForm(forms.ModelForm):

    class Meta:
        model = models.Comment
        fields = "__all__"


class CommentAdmin(admin.ModelAdmin):
    form = CommentAdminForm
    list_display = [
        "created",
        "id",
        "content",
        "last_updated",
    ]
    readonly_fields = [
        "created",
        "id",
        "content",
        "last_updated",
    ]


class LikeAdminForm(forms.ModelForm):

    class Meta:
        model = models.Like
        fields = "__all__"


class LikeAdmin(admin.ModelAdmin):
    form = LikeAdminForm
    list_display = [
        "id",
        "created",
        "last_updated",
    ]
    readonly_fields = [
        "id",
        "created",
        "last_updated",
    ]


class PostAdminForm(forms.ModelForm):

    class Meta:
        model = models.Post
        fields = "__all__"


class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = [
        "last_updated",
        "created",
        "id",
        "content",
    ]
    readonly_fields = [
        "last_updated",
        "created",
        "id",
        "content",
    ]


class TagAdminForm(forms.ModelForm):

    class Meta:
        model = models.Tag
        fields = "__all__"


class TagAdmin(admin.ModelAdmin):
    form = TagAdminForm
    list_display = [
        "last_updated",
        "name",
        "id",
        "created",
    ]
    readonly_fields = [
        "last_updated",
        "name",
        "id",
        "created",
    ]


admin.site.register(models.Comment, CommentAdmin)
admin.site.register(models.Like, LikeAdmin)
admin.site.register(models.Post, PostAdmin)
admin.site.register(models.Tag, TagAdmin)
