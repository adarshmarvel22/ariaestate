from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms
from .models import Project, ProjectImage
from .forms import ProjectForm, ProjectImageFormSet


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

    def get_context_data(self, **kwargs):
        print("testin 4g")
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["images"] = ProjectImageFormSet(self.request.POST, self.request.FILES)
        else:
            data["images"] = ProjectImageFormSet()
        return data
    
    def form_valid(self, form):
        print("testing 5")
        context = self.get_context_data()
        images = context["images"]
        self.object = form.save()
        if images.is_valid():
            images.instance = self.object
            images.save()
        return super().form_valid(form)

class ProjectDetailView(generic.DetailView):
    model = models.Project
    form_class = forms.ProjectForm


class ProjectUpdateView(generic.UpdateView):
    model = models.Project
    form_class = forms.ProjectForm
    pk_url_kwarg = "pk"

    def get_context_data(self, **kwargs):
        print("testing")
        data = super().get_context_data(**kwargs)
        if self.request.POST:
            data["images"] = ProjectImageFormSet(self.request.POST, self.request.FILES, instance=self.object)
        else:
            data["images"] = ProjectImageFormSet(instance=self.object)
        return data

    def form_valid(self, form):
        print("testing 2")
        context = self.get_context_data()
        images = context["images"]
        self.object = form.save()
        if images.is_valid():
            images.instance = self.object
            images.save()
        else:
            return self.render_to_response(self.get_context_data(form=form))
        return super().form_valid(form)


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
