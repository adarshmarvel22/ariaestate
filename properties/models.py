from django.db import models
from django.urls import reverse


class Category(models.Model):

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    description = models.TextField(max_length=100)
    name = models.CharField(max_length=30)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("properties_Category_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("properties_Category_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("properties_Category_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("properties_Category_htmx_delete", args=(self.pk,))


class Lease(models.Model):

    # Relationships
    unit = models.ForeignKey("properties.Unit", on_delete=models.CASCADE)

    # Fields
    monthly_rent = models.DecimalField(max_digits=10, decimal_places=2)
    start_date = models.DateField()
    tenant_name = models.CharField(max_length=30)
    end_date = models.DateField()
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("properties_Lease_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("properties_Lease_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("properties_Lease_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("properties_Lease_htmx_delete", args=(self.pk,))


class Project(models.Model):

    # Relationships
    category = models.ForeignKey("properties.Category", on_delete=models.CASCADE)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    launch_date = models.DateField()
    price_range = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    location = models.CharField(max_length=30)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("properties_Project_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("properties_Project_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("properties_Project_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("properties_Project_htmx_delete", args=(self.pk,))


class Unit(models.Model):

    # Relationships
    project = models.ForeignKey("properties.Project", on_delete=models.CASCADE)

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    size_sqft = models.DecimalField(max_digits=10, decimal_places=2)
    unit_number = models.CharField(max_length=30)
    is_available = models.BooleanField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("properties_Unit_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("properties_Unit_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("properties_Unit_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("properties_Unit_htmx_delete", args=(self.pk,))

class ProjectImage(models.Model):
    project = models.ForeignKey("Project", on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="project_images/", null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    def __str__(self):
        return f"Image for {self.project.title}"

    