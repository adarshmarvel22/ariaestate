from django import forms
from research.models import ResearchProject
from accounts.models import User
from research.models import ResearchProject
from accounts.models import User
from . import models


class DocumentForm(forms.ModelForm):
    class Meta:
        model = models.Document
        fields = [
            "uploaded_at",
            "file",
            "project",
        ]

    def __init__(self, *args, **kwargs):
        super(DocumentForm, self).__init__(*args, **kwargs)
        self.fields["project"].queryset = ResearchProject.objects.all()



class ResearchProjectForm(forms.ModelForm):
    class Meta:
        model = models.ResearchProject
        fields = [
            "end_date",
            "title",
            "description",
            "start_date",
            "lead",
        ]

    def __init__(self, *args, **kwargs):
        super(ResearchProjectForm, self).__init__(*args, **kwargs)
        self.fields["lead"].queryset = User.objects.all()



class TeamForm(forms.ModelForm):
    class Meta:
        model = models.Team
        fields = [
            "role",
            "project",
            "member",
        ]

    def __init__(self, *args, **kwargs):
        super(TeamForm, self).__init__(*args, **kwargs)
        self.fields["project"].queryset = ResearchProject.objects.all()
        self.fields["member"].queryset = User.objects.all()

