from django import forms
from .models import Post
from django.core.exceptions import ValidationError


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author_name',
            'category_post',
            'header',
            'content',
        ]