from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from advert.models import Advert
from advert.forms import AdvertForm



class AdvertListView(ListView):
    model = Advert
    template_name = 'adverts/list.html'
    context_object_name = 'ads'
    paginate_related_by = 4
    paginate_related_orphans = 0

    def get_queryset(self):
        return Advert.objects.all().filter(moderated=True).order_by('-post_date')


class AdvertCreateView(LoginRequiredMixin, CreateView):
    model = Advert
    template_name = 'adverts/create.html'
    form_class = AdvertForm

    def form_valid(self, form):
        ad = form.save(commit=False)
        ad.author = self.request.user
        ad.save()
        return redirect('advert_list')



class ApprovalListView(PermissionRequiredMixin, ListView):
    model = Advert
    template_name = 'adverts/approval.html'
    context_object_name = 'ads'
    paginate_related_by = 4
    paginate_related_orphans = 0
    permission_required = 'advert.approve'

    def get_queryset(self):
        return Advert.objects.all().filter(moderated=False).order_by('created_date')

    def has_permission(self):
        return super().has_permission()



class AdvertDetailView(DetailView):
    model = Advert
    template_name = 'adverts/detail.html'
    context_object_name = 'ad'


class AdvertUpdateView(PermissionRequiredMixin, UpdateView):
    model = Advert
    template_name = 'adverts/update.html'
    form_class = AdvertForm
    context_object_name = 'ad'

    def form_valid(self, form):
        ad = form.save(commit=False)
        ad.author = self.request.user
        ad.moderated = False
        ad.save()
        return redirect('advert_list')

    def has_permission(self):
        return self.get_object().author == self.request.user


class AdvertDeleteView(PermissionRequiredMixin, DeleteView):
    model = Advert
    template_name = 'adverts/delete.html'

    def get_success_url(self):
        return reverse('advert_list')

    def has_permission(self):
        return self.get_object().author == self.request.user
