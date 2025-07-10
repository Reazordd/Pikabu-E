from django import forms
from .models import Post

class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите заголовок'
            }),
            'text': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Введите текст поста'
            }),
        }
        labels = {
            'title': 'Заголовок',
            'text': 'Текст',
        }