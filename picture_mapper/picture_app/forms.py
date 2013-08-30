from django import forms
from decimal import Decimal
from easy_maps.widgets import AddressWithMapWidget

from .models import Picture
from core.forms import AuthorModelForm


class PictureForm(AuthorModelForm):
    title = forms.CharField(max_length=255)
    description = forms.Textarea()

    def clean_latitude(self):
        latitude = self.cleaned_data.get("latitude")
        if not Decimal('-90') <= latitude <= Decimal('90'):
            raise forms.ValidationError("Value not a valid latitude.")
        # Always return the cleaned data
        return self.cleaned_data["latitude"]

    def clean_longitude(self):
        longitude = self.cleaned_data.get("longitude")
        if not Decimal('-180') <= longitude <= Decimal('180'):
            raise forms.ValidationError("Value not a valid longitude.")
        # Always return the cleaned data
        return self.cleaned_data["longitude"]

    class Meta:
        model = Picture
        exclude = ('author', 'width', 'height',)