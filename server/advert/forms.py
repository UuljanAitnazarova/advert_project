from django import forms
from django.forms import ModelForm

from advert.models import Advert


class SearchForm(forms.Form):
    search_value = forms.CharField(max_length=100, required=False, label='Find')


class AdvertForm(ModelForm):
    class Meta:
        model = Advert
        fields = ['title', 'description', 'image', 'category', 'price']