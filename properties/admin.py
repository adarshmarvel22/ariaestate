from django.contrib import admin
from django import forms

from . import models


class CategoryAdminForm(forms.ModelForm):

    class Meta:
        model = models.Category
        fields = "__all__"


class CategoryAdmin(admin.ModelAdmin):
    form = CategoryAdminForm
    list_display = [
        "created",
        "id",
        "last_updated",
        "description",
        "name",
    ]
    readonly_fields = [
        "created",
        "id",
        "last_updated",
        "description",
        "name",
    ]


class LeaseAdminForm(forms.ModelForm):

    class Meta:
        model = models.Lease
        fields = "__all__"


class LeaseAdmin(admin.ModelAdmin):
    form = LeaseAdminForm
    list_display = [
        "monthly_rent",
        "start_date",
        "tenant_name",
        "end_date",
        "created",
        "id",
        "last_updated",
    ]
    readonly_fields = [
        "monthly_rent",
        "start_date",
        "tenant_name",
        "end_date",
        "created",
        "id",
        "last_updated",
    ]


class ProjectAdminForm(forms.ModelForm):

    class Meta:
        model = models.Project
        fields = "__all__"


class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = [
        "last_updated",
        "launch_date",
        "price_range",
        "title",
        "description",
        "created",
        "id",
        "location",
    ]
    readonly_fields = [
        "last_updated",
        "launch_date",
        "price_range",
        "title",
        "description",
        "created",
        "id",
        "location",
    ]


class UnitAdminForm(forms.ModelForm):

    class Meta:
        model = models.Unit
        fields = "__all__"


class UnitAdmin(admin.ModelAdmin):
    form = UnitAdminForm
    list_display = [
        "created",
        "last_updated",
        "id",
        "size_sqft",
        "unit_number",
        "is_available",
        "price",
    ]
    readonly_fields = [
        "created",
        "last_updated",
        "id",
        "size_sqft",
        "unit_number",
        "is_available",
        "price",
    ]


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Lease, LeaseAdmin)
admin.site.register(models.Project, ProjectAdmin)
admin.site.register(models.Unit, UnitAdmin)
