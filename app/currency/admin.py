from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from rangefilter.filters import DateRangeFilterBuilder

from currency.models import Rate, Source, ContactUs, RequestResponseLog


@admin.register(Rate)
class RateAdmin(ImportExportModelAdmin):
    list_display = (
        'id',
        'buy',
        'sell',
        'source',
        'currency_type',
        'created'
    )
    list_filter = (
        'currency_type',
        ('created', DateRangeFilterBuilder())
    )
    search_fields = (
        'buy',
        'sell',
        'source'
    )
    readonly_fields = (
        'buy',
        'sell'
    )


@admin.register(Source)
class SourceAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'source_url',
        'name'
    )
    search_fields = (
        'name',
    )
    readonly_fields = (
        'source_url',
    )


@admin.register(ContactUs)
class ContactusAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'email_from',
        'subject',
        'message'
    )
    search_fields = (
        'subject',
    )
    readonly_fields = (
        'email_from',
        'subject',
        'message'
    )

    def has_delete_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False


@admin.register(RequestResponseLog)
class RequestResponseLogAdmin(admin.ModelAdmin):
    list_display = (
        'path',
        'request_method',
        'time'
    )