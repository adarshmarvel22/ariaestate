from django import forms
from accounts.models import User
from accounts.models import Role
from . import models


class ProfileForm(forms.ModelForm):
    class Meta:
        model = models.Profile
        fields = [
            "avatar",
            "phone",
            "bio",
            "address",
            "user",
            "name",
        ]

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)
        self.fields["user"].queryset = User.objects.all()



class RoleForm(forms.ModelForm):
    class Meta:
        model = models.Role
        fields = [
            "name",
            "description",
        ]


class UserForm(forms.ModelForm):
    class Meta:
        model = models.User
        fields = [
            "role",
        ]

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields["role"].queryset = Role.objects.all()

