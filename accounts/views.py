from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class ProfileListView(generic.ListView):
    model = models.Profile
    form_class = forms.ProfileForm


class ProfileCreateView(generic.CreateView):
    model = models.Profile
    form_class = forms.ProfileForm


class ProfileDetailView(generic.DetailView):
    model = models.Profile
    form_class = forms.ProfileForm


class ProfileUpdateView(generic.UpdateView):
    model = models.Profile
    form_class = forms.ProfileForm
    pk_url_kwarg = "pk"


class ProfileDeleteView(generic.DeleteView):
    model = models.Profile
    success_url = reverse_lazy("accounts_Profile_list")


class RoleListView(generic.ListView):
    model = models.Role
    form_class = forms.RoleForm


class RoleCreateView(generic.CreateView):
    model = models.Role
    form_class = forms.RoleForm


class RoleDetailView(generic.DetailView):
    model = models.Role
    form_class = forms.RoleForm


class RoleUpdateView(generic.UpdateView):
    model = models.Role
    form_class = forms.RoleForm
    pk_url_kwarg = "pk"


class RoleDeleteView(generic.DeleteView):
    model = models.Role
    success_url = reverse_lazy("accounts_Role_list")


class UserListView(generic.ListView):
    model = models.User
    form_class = forms.UserForm


class UserCreateView(generic.CreateView):
    model = models.User
    form_class = forms.UserForm


class UserDetailView(generic.DetailView):
    model = models.User
    form_class = forms.UserForm


class UserUpdateView(generic.UpdateView):
    model = models.User
    form_class = forms.UserForm
    pk_url_kwarg = "pk"


class UserDeleteView(generic.DeleteView):
    model = models.User
    success_url = reverse_lazy("accounts_User_list")
