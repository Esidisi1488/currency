from django.db import models
from django.utils.translation import gettext_lazy as _
from django.templatetags.static import static

from currency.choices import CurrencyTypeChoices


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return f'logos/{instance.name}/{filename}'


class Rate(models.Model):
    buy = models.DecimalField(_('Buy'), max_digits=6, decimal_places=2)
    sell = models.DecimalField(_('Sell'), max_digits=6, decimal_places=2)
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    currency_type = models.SmallIntegerField(
        _('Currency type'),
        choices=CurrencyTypeChoices.choices,
        default=CurrencyTypeChoices.USD
    )
    source = models.ForeignKey('currency.Source', on_delete=models.CASCADE, related_name='rates')

    class Meta:
        verbose_name = _('Rate')
        verbose_name_plural = _('Rates')

    def __str__(self):
        return f'{self.buy} - {self.sell} - {self.source}'


class ContactUs(models.Model):
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    name = models.CharField(_('Name'), max_length=64)
    email_from = models.EmailField(_('Email from'), max_length=128)
    subject = models.CharField(_('Subject'), max_length=256)
    message = models.CharField(_('Message'), max_length=2048)

    class Meta:
        verbose_name = _('Contact Us')
        verbose_name_plural = _('Contact Us')


class Source(models.Model):
    source_url = models.CharField(_('Source url'), max_length=255)
    name = models.CharField(_('Name'), max_length=64)
    logo = models.FileField(_('Logo'), default=None, null=True, blank=True, upload_to=user_directory_path)

    class Meta:
        verbose_name = _('Source')
        verbose_name_plural = _('Sources')

    def __str__(self):
        return self.name

    @property
    def logo_url(self) -> str:
        if self.logo:
            return self.logo.url

        return static('Privat24_Logo.png')


class RequestResponseLog(models.Model):
    path = models.CharField(_('Path'), max_length=255)
    request_method = models.CharField(_('Request method'), max_length=64)
    time = models.DecimalField(_('Time'), max_digits=14, decimal_places=10)
# Create your models here.
