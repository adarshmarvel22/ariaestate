from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class Profile(models.Model):

    # Relationships
    user = models.OneToOneField("accounts.User", on_delete=models.CASCADE)

    # Fields
    avatar = models.ImageField(upload_to="upload/images/")
    name = models.CharField(max_length=30, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    phone = models.CharField(max_length=30)
    bio = models.TextField(max_length=100)
    address = models.TextField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("accounts_Profile_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("accounts_Profile_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("accounts_Profile_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("accounts_Profile_htmx_delete", args=(self.pk,))
    
    def save(self, *args, **kwargs):
        if not self.name:
            self.name = f"AriaEstate Guest: {self.pk or ''}"
        super().save(*args, **kwargs)


class Role(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    name = models.CharField(max_length=30)
    description = models.TextField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("accounts_Role_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("accounts_Role_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("accounts_Role_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("accounts_Role_htmx_delete", args=(self.pk,))


class User(AbstractUser):

    def get_default_role():
        return Role.objects.get_or_create(name="Customer")[0].id

    # Relationships
    role = models.ForeignKey("accounts.Role", on_delete=models.CASCADE, default=get_default_role)
    # profile = models.ForeignKey("accounts.Profile", on_delete=models.CASCADE, null=True, blank=True)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("accounts_User_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("accounts_User_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("accounts_User_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("accounts_User_htmx_delete", args=(self.pk,))
