from django.views.generic import (
    ListView, CreateView, UpdateView,
    DeleteView, DetailView, TemplateView
)
from django.urls import reverse_lazy
from currency.models import Rate, ContactUs, Source
from currency.forms import RateForm, SourceForm, ContactusForm


# RATE
class RateListView(ListView):
    queryset = Rate.objects.all()
    template_name = 'rate_list.html'


class RateCreateView(CreateView):
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_create.html'


class RateUpdateView(UpdateView):
    model = Rate
    form_class = RateForm
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_update.html'


class RateDeleteView(DeleteView):
    model = Rate
    success_url = reverse_lazy('currency:rate-list')
    template_name = 'rate_delete.html'


class RateDetailsView(DetailView):
    model = Rate
    template_name = 'rate_details.html'


# ContactUs
class ContactusListView(ListView):
    queryset = ContactUs.objects.all()
    template_name = 'contactus_list.html'


class ContactusCreateView(CreateView):
    form_class = ContactusForm
    success_url = reverse_lazy('contactus-list')
    template_name = 'contactus_create.html'


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
# Create your views here.
