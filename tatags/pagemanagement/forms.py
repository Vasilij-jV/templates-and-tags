from django import forms
from .models import Page


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        fields = ['title', 'content', 'slug']


class DeletePage(forms.Form):
    enter = forms.CharField(max_length=100)
