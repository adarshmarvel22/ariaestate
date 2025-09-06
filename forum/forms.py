from django import forms
from forum.models import Post
from accounts.models import User
from forum.models import Post
from accounts.models import User
from accounts.models import User
from forum.models import Tag
from . import models


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = [
            "content",
            "post",
            "author",
        ]

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields["post"].queryset = Post.objects.all()
        self.fields["author"].queryset = User.objects.all()



class LikeForm(forms.ModelForm):
    class Meta:
        model = models.Like
        fields = [
            "post",
            "user",
        ]

    def __init__(self, *args, **kwargs):
        super(LikeForm, self).__init__(*args, **kwargs)
        self.fields["post"].queryset = Post.objects.all()
        self.fields["user"].queryset = User.objects.all()



class PostForm(forms.ModelForm):
    class Meta:
        model = models.Post
        fields = [
            "content",
            "author",
            "tags",
        ]

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields["author"].queryset = User.objects.all()
        self.fields["tags"].queryset = Tag.objects.all()



class TagForm(forms.ModelForm):
    class Meta:
        model = models.Tag
        fields = [
            "name",
        ]
