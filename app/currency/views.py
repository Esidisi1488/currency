from datetime import datetime, timedelta
from django.views.generic import (
    ListView, CreateView, UpdateView,
    DeleteView, DetailView, TemplateView
)

# from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import UserPassesTestMixin

from django.urls import reverse_lazy
from time import time
from currency.tasks import send_email_in_background
from currency.models import Rate, ContactUs, Source
from currency.forms import RateForm, SourceForm, ContactusForm


# RATE
class RateListView(LoginRequiredMixin, ListView):
    queryset = Rate.objects.all().select_related('source')
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
        '''
        | 00:00 - 07:59 | 08:00 - 17:59 | 18:00 - 23:59 |
        | eta - 8:00    |  now          | eta - 8:00 next day|
        '''
        from django.conf import settings
        recipient = settings.DEFAULT_FROM_EMAIL
        subject = 'User contact us'
        body = f'''
                Name: {self.object.name}
                Email: {self.object.email_from}
                Subject: {self.object.subject}
                Message: {self.object.message}
                '''
        eta = datetime.now() + timedelta(seconds=60)
        send_email_in_background.apply_async(
            kwargs={
                'subject': subject,
                'body': body
            }
        )

    def form_valid(self, form):
        redirect = super().form_valid(form)

        self._send_email()

        return redirect


class ContactusUpdateView(UpdateView):
    model = ContactUs
    form_class = ContactusForm
    success_url = reverse_lazy('currency:contactus-list')
    template_name = 'contactus_update.html'


class ContactusDeleteView(DeleteView):
    model = ContactUs
    success_url = reverse_lazy('currency:contactus-list')
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
    success_url = reverse_lazy('currency:source-list')
    template_name = 'source_create.html'


class SourceUpdateView(UpdateView):
    model = Source
    form_class = SourceForm
    success_url = reverse_lazy('currency:source-list')
    template_name = 'source_update.html'


class SourceDeleteView(DeleteView):
    model = Source
    success_url = reverse_lazy('currency:source-list')
    template_name = 'source_delete.html'


class SourceDetailsView(DetailView):
    model = Source
    template_name = 'source_details.html'


class IndexView(TemplateView):
    template_name = 'index.html'


# Create your views here.
