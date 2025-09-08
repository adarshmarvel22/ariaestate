from django import forms
from properties.models import Unit
from properties.models import Category
from properties.models import Project, ProjectImage
from . import models


class CategoryForm(forms.ModelForm):
    class Meta:
        model = models.Category
        fields = [
            "description",
            "name",
        ]


class LeaseForm(forms.ModelForm):
    class Meta:
        model = models.Lease
        fields = [
            "monthly_rent",
            "start_date",
            "tenant_name",
            "end_date",
            "unit",
        ]

    def __init__(self, *args, **kwargs):
        super(LeaseForm, self).__init__(*args, **kwargs)
        self.fields["unit"].queryset = Unit.objects.all()



class ProjectForm(forms.ModelForm):
    class Meta:
        model = models.Project
        fields = [
            "launch_date",
            "price_range",
            "title",
            "description",
            "location",
            "category",
        ]

    def __init__(self, *args, **kwargs):
        super(ProjectForm, self).__init__(*args, **kwargs)
        self.fields["category"].queryset = Category.objects.all()



class UnitForm(forms.ModelForm):
    class Meta:
        model = models.Unit
        fields = [
            "size_sqft",
            "unit_number",
            "is_available",
            "price",
            "project",
        ]

    def __init__(self, *args, **kwargs):
        super(UnitForm, self).__init__(*args, **kwargs)
        self.fields["project"].queryset = Project.objects.all()


class ProjectImageForm(forms.ModelForm):
    class Meta:
        model = ProjectImage
        fields = ["image"]


ProjectImageFormSet = forms.inlineformset_factory(
    Project,
    ProjectImage,
    form=ProjectImageForm,
    extra=3,   # show 3 empty fields by default
    can_delete=True,
)
