from django.forms import ModelForm

from advert.models import Advert


class AdvertForm(ModelForm):
    class Meta:
        model = Advert
        fields = ['title', 'description', 'image', 'category', 'price']