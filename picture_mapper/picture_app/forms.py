from django import forms
from .models import Picture
from core.forms import AuthorModelForm


class PictureForm(AuthorModelForm):
    title = forms.CharField(max_length=255)
    description = forms.Textarea()

    class Meta:
        model = Picture
        exclude = ('author', 'width', 'height',)