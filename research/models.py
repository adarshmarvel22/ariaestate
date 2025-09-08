from django.db import models
from django.urls import reverse


class Document(models.Model):

    # Relationships
    project = models.ForeignKey("research.ResearchProject", on_delete=models.CASCADE)

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    uploaded_at = models.DateTimeField()
    file = models.FileField(upload_to="files/")

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("research_Document_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("research_Document_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("research_Document_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("research_Document_htmx_delete", args=(self.pk,))


class ResearchProject(models.Model):

    # Relationships
    lead = models.ForeignKey("accounts.User", on_delete=models.SET_NULL, null=True, related_name="lead_projects")

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    end_date = models.DateField(null=True, blank=True)
    title = models.CharField(max_length=30)
    description = models.TextField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    start_date = models.DateField()

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("research_ResearchProject_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("research_ResearchProject_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("research_ResearchProject_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("research_ResearchProject_htmx_delete", args=(self.pk,))


class Team(models.Model):

    # Relationships
    project = models.ForeignKey("research.ResearchProject", on_delete=models.CASCADE)
    member = models.ForeignKey("accounts.User", on_delete=models.CASCADE)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    role = models.CharField(max_length=30)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("research_Team_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("research_Team_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("research_Team_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("research_Team_htmx_delete", args=(self.pk,))
