# Generated by Django 4.2.7 on 2024-03-20 13:45

import currency.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('email_from', models.EmailField(max_length=128, verbose_name='Email from')),
                ('subject', models.CharField(max_length=256, verbose_name='Subject')),
                ('message', models.CharField(max_length=2048, verbose_name='Message')),
            ],
            options={
                'verbose_name': 'Contact Us',
                'verbose_name_plural': 'Contact Us',
            },
        ),
        migrations.CreateModel(
            name='RequestResponseLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255, verbose_name='Path')),
                ('request_method', models.CharField(max_length=64, verbose_name='Request method')),
                ('time', models.DecimalField(decimal_places=10, max_digits=14, verbose_name='Time')),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source_url', models.CharField(max_length=255, verbose_name='Source url')),
                ('name', models.CharField(max_length=64, verbose_name='Name')),
                ('code_name', models.CharField(max_length=64, unique=True, verbose_name='Code name')),
                ('logo', models.FileField(blank=True, default=None, null=True, upload_to=currency.models.user_directory_path, verbose_name='Logo')),
            ],
            options={
                'verbose_name': 'Source',
                'verbose_name_plural': 'Sources',
            },
        ),
        migrations.CreateModel(
            name='Rate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buy', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Buy')),
                ('sell', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Sell')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Created')),
                ('currency_type', models.SmallIntegerField(choices=[(2, 'Dollar'), (1, 'Euro')], default=2, verbose_name='Currency type')),
                ('source', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rates', to='currency.source')),
            ],
            options={
                'verbose_name': 'Rate',
                'verbose_name_plural': 'Rates',
            },
        ),
    ]
