from django.urls import path


from currency.views import (
    RateListView,
    RateCreateView,
    RateUpdateView,
    RateDeleteView,
    RateDetailsView,
    ContactusListView,
    ContactusCreateView,
    ContactusUpdateView,
    ContactusDeleteView,
    ContactusDetailsView,
    SourceListView,
    SourceCreateView,
    SourceUpdateView,
    SourceDeleteView,
    SourceDetailsView,

)

app_name = 'currency'

urlpatterns = [
    path('rate/list/', RateListView.as_view(), name='rate-list'),
    path('rate/create/', RateCreateView.as_view(), name='rate-create'),
    path('rate/update/<int:pk>/', RateUpdateView.as_view(), name='rate-update'),
    path('rate/delete/<int:pk>/', RateDeleteView.as_view(), name='rate-delete'),
    path('rate/details/<int:pk>/', RateDetailsView.as_view(), name='rate-details'),
    path('source/list/', SourceListView.as_view(), name='source-list'),
    path('source/create/', SourceCreateView.as_view(), name='source-create'),
    path('source/update/<int:pk>/', SourceUpdateView.as_view(), name='source-update'),
    path('source/delete/<int:pk>/', SourceDeleteView.as_view(), name='source-delete'),
    path('source/details/<int:pk>/', SourceDetailsView.as_view(), name='source-details'),
    path('contactus/list/', ContactusListView.as_view(), name='contactus-list'),
    path('contactus/create/', ContactusCreateView.as_view(), name='contactus-create'),
    path('contactus/update/<int:pk>/', ContactusUpdateView.as_view(), name='contactus-update'),
    path('contactus/delete/<int:pk>/', ContactusDeleteView.as_view(), name='contactus-delete'),
    path('contactus/details/<int:pk>/', ContactusDetailsView.as_view(), name='contactus-details'),
]
