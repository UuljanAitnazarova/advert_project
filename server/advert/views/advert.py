from datetime import datetime

from django.http import JsonResponse
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.utils.http import urlencode
from django.views.generic import ListView, CreateView, DetailView, DeleteView, UpdateView

from advert.models import Advert
from advert.forms import AdvertForm, SearchForm


class AdvertListView(ListView):
    model = Advert
    template_name = 'adverts/list.html'
    context_object_name = 'ads'
    paginate_related_by = 4
    paginate_related_orphans = 0


    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(AdvertListView, self).get(request, **kwargs)


    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_data:
            queryset = queryset.filter(
                Q(title__icontains=self.search_data)
            )
        return queryset.filter(moderated=True).order_by('-post_date')

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['adverts'] = Advert.objects.all().filter(moderated=True).order_by('-post_date')
        context['search_form'] = self.form

        if self.search_data:
            context['query'] = urlencode({'search_value': self.search_data})
        return context



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

    def get(self, request, **kwargs):
        self.form = SearchForm(request.GET)
        self.search_data = self.get_search_data()
        return super(ApprovalListView, self).get(request, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.search_data:
            queryset = queryset.filter(
                Q(title__icontains=self.search_data)
            )
        return queryset.filter(moderated=False).order_by('created_date')

    def get_search_data(self):
        if self.form.is_valid():
            return self.form.cleaned_data['search_value']
        return None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['adverts'] = Advert.objects.all().filter(moderated=False).order_by('created_date')
        context['search_form'] = self.form

        if self.search_data:
            context['query'] = urlencode({'search_value': self.search_data})
        return context

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


class ApprovalAdvertDetailView(PermissionRequiredMixin, DetailView):
    model = Advert
    template_name = 'adverts/approval_detail.html'
    context_object_name = 'ad'
    permission_required = 'advert.approve'

    def has_permission(self):
        return super().has_permission()


def approve(request, *args, **kwargs):
    if request.is_ajax and request.method == "POST":
        ad = get_object_or_404(Advert, pk=list(dict(request.POST).keys())[0])
        ad.moderated = True
        ad.published_at = datetime.now()
        ad.save()
        return JsonResponse({'message': 'Success!'}, status=200)
    return JsonResponse({"error": ""}, status=400, safe=False)


def reject(request, *args, **kwargs):
    if request.is_ajax and request.method == "POST":
        ad = get_object_or_404(Advert, pk=list(dict(request.POST).keys())[0])
        ad.rejected = True
        ad.save()
        return JsonResponse({'message': 'Rejected'}, status=200)
    return JsonResponse({"error": ""}, status=400, safe=False)