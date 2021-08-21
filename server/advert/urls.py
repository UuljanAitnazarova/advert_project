from django.contrib import admin
from django.urls import path, include

from advert.views.advert import AdvertCreateView, AdvertListView

urlpatterns = [
    path('', AdvertListView.as_view(), name='advert_list'),
    path('create/', AdvertCreateView.as_view(), name='advert_create'),
]