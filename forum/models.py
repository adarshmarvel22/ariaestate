from django.db import models
from django.urls import reverse


class Comment(models.Model):

    # Relationships
    post = models.ForeignKey("forum.Post", on_delete=models.CASCADE)
    author = models.ForeignKey("accounts.User", on_delete=models.CASCADE)

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    content = models.TextField(max_length=100)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("forum_Comment_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("forum_Comment_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("forum_Comment_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("forum_Comment_htmx_delete", args=(self.pk,))


class Like(models.Model):

    # Relationships
    post = models.ForeignKey("forum.Post", on_delete=models.CASCADE)
    user = models.ForeignKey("accounts.User", on_delete=models.CASCADE)

    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    last_updated = models.DateTimeField(auto_now=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("forum_Like_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("forum_Like_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("forum_Like_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("forum_Like_htmx_delete", args=(self.pk,))


class Post(models.Model):

    # Relationships
    author = models.ForeignKey("accounts.User", on_delete=models.CASCADE)
    tags = models.ManyToManyField("forum.Tag", blank=True)

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    created = models.DateTimeField(auto_now_add=True, editable=False)
    content = models.TextField(max_length=100)

    class Meta:
        pass

    def __str__(self):
        return str(self.pk)

    def get_absolute_url(self):
        return reverse("forum_Post_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("forum_Post_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("forum_Post_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("forum_Post_htmx_delete", args=(self.pk,))


class Tag(models.Model):

    # Fields
    last_updated = models.DateTimeField(auto_now=True, editable=False)
    name = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    class Meta:
        pass

    def __str__(self):
        return str(self.name)

    def get_absolute_url(self):
        return reverse("forum_Tag_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("forum_Tag_update", args=(self.pk,))

    @staticmethod
    def get_htmx_create_url():
        return reverse("forum_Tag_htmx_create")

    def get_htmx_delete_url(self):
        return reverse("forum_Tag_htmx_delete", args=(self.pk,))
