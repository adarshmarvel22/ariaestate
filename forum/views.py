from django.views import generic
from django.urls import reverse_lazy
from . import models
from . import forms


class CommentListView(generic.ListView):
    model = models.Comment
    form_class = forms.CommentForm


class CommentCreateView(generic.CreateView):
    model = models.Comment
    form_class = forms.CommentForm


class CommentDetailView(generic.DetailView):
    model = models.Comment
    form_class = forms.CommentForm


class CommentUpdateView(generic.UpdateView):
    model = models.Comment
    form_class = forms.CommentForm
    pk_url_kwarg = "pk"


class CommentDeleteView(generic.DeleteView):
    model = models.Comment
    success_url = reverse_lazy("forum_Comment_list")


class LikeListView(generic.ListView):
    model = models.Like
    form_class = forms.LikeForm


class LikeCreateView(generic.CreateView):
    model = models.Like
    form_class = forms.LikeForm


class LikeDetailView(generic.DetailView):
    model = models.Like
    form_class = forms.LikeForm


class LikeUpdateView(generic.UpdateView):
    model = models.Like
    form_class = forms.LikeForm
    pk_url_kwarg = "pk"


class LikeDeleteView(generic.DeleteView):
    model = models.Like
    success_url = reverse_lazy("forum_Like_list")


class PostListView(generic.ListView):
    model = models.Post
    form_class = forms.PostForm


class PostCreateView(generic.CreateView):
    model = models.Post
    form_class = forms.PostForm


class PostDetailView(generic.DetailView):
    model = models.Post
    form_class = forms.PostForm


class PostUpdateView(generic.UpdateView):
    model = models.Post
    form_class = forms.PostForm
    pk_url_kwarg = "pk"


class PostDeleteView(generic.DeleteView):
    model = models.Post
    success_url = reverse_lazy("forum_Post_list")


class TagListView(generic.ListView):
    model = models.Tag
    form_class = forms.TagForm


class TagCreateView(generic.CreateView):
    model = models.Tag
    form_class = forms.TagForm


class TagDetailView(generic.DetailView):
    model = models.Tag
    form_class = forms.TagForm


class TagUpdateView(generic.UpdateView):
    model = models.Tag
    form_class = forms.TagForm
    pk_url_kwarg = "pk"


class TagDeleteView(generic.DeleteView):
    model = models.Tag
    success_url = reverse_lazy("forum_Tag_list")
