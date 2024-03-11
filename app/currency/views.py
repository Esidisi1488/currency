from django.views.generic import (
    ListView, CreateView, UpdateView,
    DeleteView, DetailView, TemplateView
)

# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin

from django.urls import reverse_lazy
from django.core.mail import send_mail
from time import time
from currency.models import Rate, ContactUs, Source
from currency.forms import RateForm, SourceForm, ContactusForm


# RATE
class RateListView(LoginRequiredMixin, ListView):
    queryset = Rate.objects.all()
    template_name = 'rate_list.html'


class RateCreateView(LoginRequiredMixin, CreateView):
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_create.html'


class RateUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    def test_func(self):
        return self.request.user.is_superuser

    model = Rate
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_update.html'


class RateDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    def test_func(self):
        return self.request.user.is_superuser

    model = Rate
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_delete.html'


class RateDetailsView(LoginRequiredMixin, DetailView):
    model = Rate
    template_name = 'rate_details.html'


# ContactUs
class ContactusListView(ListView):
    queryset = ContactUs.objects.all()
    template_name = 'contactus_list.html'


class TimeItMixin:

    def dispatch(self, request, *args, **kwargs):
        print('BEFORE IN VIEW')
        start = time()

        response = super().dispatch(request, *args, **kwargs)

        end = time()
        print(f'AFTER IN VIEW {end - start}')

        return response


class ContactusCreateView(TimeItMixin, CreateView):
    form_class = ContactusForm
    success_url = reverse_lazy('index')
    template_name = 'contactus_create.html'

    def _send_email(self):
        from django.conf import settings
        recipient = settings.DEFAULT_FROM_EMAIL
        subject = 'User contact us'
        body = f'''
                Name: {self.object.name}
                Email: {self.object.email_from}
                Subject: {self.object.subject}
                Message: {self.object.message}
                '''

        send_mail(
            subject,
            body,
            recipient,
            [recipient],
            fail_silently=False,
        )

    def form_valid(self, form):
        redirect = super().form_valid(form)

        self._send_email()

        return redirect


class ContactusUpdateView(UpdateView):
    model = ContactUs
    form_class = ContactusForm
    success_url = reverse_lazy('contactus-list')
    template_name = 'contactus_update.html'


class ContactusDeleteView(DeleteView):
    model = ContactUs
    success_url = reverse_lazy('contactus-list')
    template_name = 'contactus_delete.html'


class ContactusDetailsView(DetailView):
    model = ContactUs
    template_name = 'contactus_details.html'


# Source
class SourceListView(ListView):
    queryset = Source.objects.all()
    template_name = 'source_list.html'


class SourceCreateView(CreateView):
    form_class = SourceForm
    success_url = reverse_lazy('source-list')
    template_name = 'source_create.html'


class SourceUpdateView(UpdateView):
    model = Source
    form_class = SourceForm
    success_url = reverse_lazy('source-list')
    template_name = 'source_update.html'


class SourceDeleteView(DeleteView):
    model = Source
    success_url = reverse_lazy('source-list')
    template_name = 'source_delete.html'


class SourceDetailsView(DetailView):
    model = Source
    template_name = 'source_details.html'


class IndexView(TemplateView):
    template_name = 'index.html'


class ProfileView(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    template_name = 'profile.html'
    success_url = reverse_lazy('index')
    fields = (
        'first_name',
        'last_name'
    )

    # def get_queryset(self):
    #     qs = super().get_queryset().filter(id=self.request.user.id)
    #     return qs

    def get_object(self, queryset=None):
        qs = self.get_queryset()

        return qs.get(id=self.request.user.id)

# Create your views here.
