from django import forms
from .models import Post, SubscribersCategory


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            'author_name',
            'category_post',
            'header',
            'content',
        ]


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = SubscribersCategory
        fields = ['category']
