from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class CategoryListView(generic.ListView):
    model = models.Category
    form_class = forms.CategoryForm


class CategoryCreateView(generic.CreateView):
    model = models.Category
    form_class = forms.CategoryForm


class CategoryDetailView(generic.DetailView):
    model = models.Category
    form_class = forms.CategoryForm


class CategoryUpdateView(generic.UpdateView):
    model = models.Category
    form_class = forms.CategoryForm
    pk_url_kwarg = "pk"


class CategoryDeleteView(generic.DeleteView):
    model = models.Category
    success_url = reverse_lazy("properties_Category_list")


class LeaseListView(generic.ListView):
    model = models.Lease
    form_class = forms.LeaseForm


class LeaseCreateView(generic.CreateView):
    model = models.Lease
    form_class = forms.LeaseForm


class LeaseDetailView(generic.DetailView):
    model = models.Lease
    form_class = forms.LeaseForm


class LeaseUpdateView(generic.UpdateView):
    model = models.Lease
    form_class = forms.LeaseForm
    pk_url_kwarg = "pk"


class LeaseDeleteView(generic.DeleteView):
    model = models.Lease
    success_url = reverse_lazy("properties_Lease_list")


class ProjectListView(generic.ListView):
    model = models.Project
    form_class = forms.ProjectForm


class ProjectCreateView(generic.CreateView):
    model = models.Project
    form_class = forms.ProjectForm


class ProjectDetailView(generic.DetailView):
    model = models.Project
    form_class = forms.ProjectForm


class ProjectUpdateView(generic.UpdateView):
    model = models.Project
    form_class = forms.ProjectForm
    pk_url_kwarg = "pk"


class ProjectDeleteView(generic.DeleteView):
    model = models.Project
    success_url = reverse_lazy("properties_Project_list")


class UnitListView(generic.ListView):
    model = models.Unit
    form_class = forms.UnitForm


class UnitCreateView(generic.CreateView):
    model = models.Unit
    form_class = forms.UnitForm


class UnitDetailView(generic.DetailView):
    model = models.Unit
    form_class = forms.UnitForm


class UnitUpdateView(generic.UpdateView):
    model = models.Unit
    form_class = forms.UnitForm
    pk_url_kwarg = "pk"


class UnitDeleteView(generic.DeleteView):
    model = models.Unit
    success_url = reverse_lazy("properties_Unit_list")
