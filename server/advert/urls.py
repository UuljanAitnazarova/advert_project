from django.contrib import admin
from django.urls import path, include

from advert.views.advert import AdvertCreateView, AdvertListView, ApprovalListView, \
    AdvertDetailView, AdvertUpdateView, AdvertDeleteView, ApprovalAdvertDetailView, \
    approve, reject

urlpatterns = [
    path('', AdvertListView.as_view(), name='advert_list'),
    path('create/', AdvertCreateView.as_view(), name='advert_create'),
    path('approve/', ApprovalListView.as_view(), name='advert_approve'),
    path('<int:pk>/', AdvertDetailView.as_view(), name='advert_detail'),
    path('<int:pk>/update/', AdvertUpdateView.as_view(), name='advert_update'),
    path('<int:pk>/delete/', AdvertDeleteView.as_view(), name='advert_delete'),
    path('approve/<int:pk>/', ApprovalAdvertDetailView.as_view(), name='approve_detail'),
    path('approve/', approve, name='approve'),
    path('reject/', reject, name='reject')
]


