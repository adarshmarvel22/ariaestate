from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class DocumentListView(generic.ListView):
    model = models.Document
    form_class = forms.DocumentForm


class DocumentCreateView(generic.CreateView):
    model = models.Document
    form_class = forms.DocumentForm


class DocumentDetailView(generic.DetailView):
    model = models.Document
    form_class = forms.DocumentForm


class DocumentUpdateView(generic.UpdateView):
    model = models.Document
    form_class = forms.DocumentForm
    pk_url_kwarg = "pk"


class DocumentDeleteView(generic.DeleteView):
    model = models.Document
    success_url = reverse_lazy("research_Document_list")


class ResearchProjectListView(generic.ListView):
    model = models.ResearchProject
    form_class = forms.ResearchProjectForm


class ResearchProjectCreateView(generic.CreateView):
    model = models.ResearchProject
    form_class = forms.ResearchProjectForm


class ResearchProjectDetailView(generic.DetailView):
    model = models.ResearchProject
    form_class = forms.ResearchProjectForm


class ResearchProjectUpdateView(generic.UpdateView):
    model = models.ResearchProject
    form_class = forms.ResearchProjectForm
    pk_url_kwarg = "pk"


class ResearchProjectDeleteView(generic.DeleteView):
    model = models.ResearchProject
    success_url = reverse_lazy("research_ResearchProject_list")


class TeamListView(generic.ListView):
    model = models.Team
    form_class = forms.TeamForm


class TeamCreateView(generic.CreateView):
    model = models.Team
    form_class = forms.TeamForm


class TeamDetailView(generic.DetailView):
    model = models.Team
    form_class = forms.TeamForm


class TeamUpdateView(generic.UpdateView):
    model = models.Team
    form_class = forms.TeamForm
    pk_url_kwarg = "pk"


class TeamDeleteView(generic.DeleteView):
    model = models.Team
    success_url = reverse_lazy("research_Team_list")
