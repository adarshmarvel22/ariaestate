from django.contrib import admin
from django import forms

from . import models


class ProfileAdminForm(forms.ModelForm):

    class Meta:
        model = models.Profile
        fields = "__all__"


class ProfileAdmin(admin.ModelAdmin):
    form = ProfileAdminForm
    list_display = [
        "avatar",
        "created",
        "last_updated",
        "phone",
        "bio",
        "id",
        "address",
    ]
    readonly_fields = [
        "avatar",
        "created",
        "last_updated",
        "phone",
        "bio",
        "id",
        "address",
    ]


class RoleAdminForm(forms.ModelForm):

    class Meta:
        model = models.Role
        fields = "__all__"


class RoleAdmin(admin.ModelAdmin):
    form = RoleAdminForm
    list_display = [
        "id",
        "created",
        "last_updated",
        "name",
        "description",
    ]
    readonly_fields = [
        "id",
        "created",
        "last_updated",
        "name",
        "description",
    ]


class UserAdminForm(forms.ModelForm):

    class Meta:
        model = models.User
        fields = "__all__"


class UserAdmin(admin.ModelAdmin):
    form = UserAdminForm
    list_display = [
        "id",
        "last_updated",
        "created",
    ]
    readonly_fields = [
        "id",
        "last_updated",
        "created",
    ]


admin.site.register(models.Profile, ProfileAdmin)
admin.site.register(models.Role, RoleAdmin)
admin.site.register(models.User, UserAdmin)
