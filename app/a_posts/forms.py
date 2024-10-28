from django import forms
from django.forms import ModelForm
from .models import *


class PostCreateForm(ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['url', 'body', 'tags']
        labels = {
            'body': 'Caption',
            'tags': 'Category',
        }
        widgets = {
            'url': forms.TextInput(attrs={
                'placeholder': 'Add a URL...',
            }),
            'body': forms.Textarea(attrs={
                'rows': 3,
                'placeholder': 'Add a caption...',
                'class': 'font1 text-4xl'
            }),
            'tags': forms.CheckboxSelectMultiple()
        }



class PostEditForm(ModelForm):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['body', 'tags']
        labels = {
            'body': '',
            'tags': 'Category',
        }
        widgets = {
            'body': forms.Textarea(attrs={
                'rows': 3,
                'class': 'font1 text-4xl'
            }),
            'tags': forms.CheckboxSelectMultiple()
        }


class CommentCreateForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
        labels = {
            'body': '',
        }
        widgets = {
            'body': forms.TextInput(attrs={'placeholder': 'Add a comment...'}),
        }
        
        
class ReplyCreateForm(ModelForm):
    class Meta:
        model = Reply
        fields = ['body']
        labels = {
            'body': '',
        }
        widgets = {
            'body': forms.TextInput(attrs={'placeholder': 'Add a reply...', 'class': 'text-sm'}),
        }

