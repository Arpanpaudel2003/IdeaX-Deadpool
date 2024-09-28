from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'para']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','placeholder':'Enter the post title'}),
            'para': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Enter the post content'}),
        }