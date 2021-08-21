from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse
from django.views.generic import DetailView, UpdateView

from advert.models import Advert
from accounts.models import Profile
from accounts.forms import ProfileForm


class UserProfileView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = 'profile.html'
    context_object_name = 'user_obj'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        adverts = Advert.objects.all()
        user_obj = self.get_object()
        if self.request.user == user_obj:
            context['adverts'] = adverts.filter(author=user_obj)
            return context
        context['adverts'] = adverts.filter(moderated=True, author=user_obj)
        return context



class ProfileUpdateView(PermissionRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'update.html'
    permission_required = 'accounts.change_profile'


    def has_permission(self):
        return self.get_object().user == self.request.user

    def get_success_url(self):
        return reverse('profile', kwargs={'pk': self.get_object().pk})