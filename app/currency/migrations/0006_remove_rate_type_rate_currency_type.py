# Generated by Django 4.2.7 on 2023-12-14 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0005_source'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rate',
            name='type',
        ),
        migrations.AddField(
            model_name='rate',
            name='currency_type',
            field=models.SmallIntegerField(choices=[(2, 'Dollar'), (1, 'Euro')], default=2),
        ),
    ]
