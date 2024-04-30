from django import forms
from .models import Post

# Simple form that contains necessary fields for Post object creation
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'message']