from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import DetailView

from advert.models import Advert


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

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     if self.request.user == get_user_model():
    #         context['adverts'] = get_user_model().objects.get
    #         return context
    #     context['adverts'] = get_user_model().advert.filter(moderated=True)
    #     return context



