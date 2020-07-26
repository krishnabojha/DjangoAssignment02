from django import forms
from .models import Blog, AuthorDetail

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'author', 'description']

class AuthorDetailForm(forms.ModelForm):
    class Meta:
        model = AuthorDetail
        fields = ['profile_img', 'address', 'email']