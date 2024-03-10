# Generated by Django 4.2.7 on 2024-03-10 19:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0006_remove_rate_type_rate_currency_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contactus',
            options={'verbose_name': 'Contact Us', 'verbose_name_plural': 'Contact Us'},
        ),
        migrations.AlterModelOptions(
            name='rate',
            options={'verbose_name': 'Rate', 'verbose_name_plural': 'Rates'},
        ),
        migrations.AlterModelOptions(
            name='source',
            options={'verbose_name': 'Source', 'verbose_name_plural': 'Sources'},
        ),
        migrations.AddField(
            model_name='contactus',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactus',
            name='name',
            field=models.CharField(default='Oleh', max_length=64, verbose_name='Name'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contactus',
            name='email_from',
            field=models.EmailField(max_length=128, verbose_name='Email from'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='message',
            field=models.CharField(max_length=2048, verbose_name='Message'),
        ),
        migrations.AlterField(
            model_name='contactus',
            name='subject',
            field=models.CharField(max_length=256, verbose_name='Subject'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='buy',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Buy'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='currency_type',
            field=models.SmallIntegerField(choices=[(2, 'Dollar'), (1, 'Euro')], default=2, verbose_name='Currency type'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='sell',
            field=models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Sell'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='source',
            field=models.CharField(max_length=255, verbose_name='Source'),
        ),
        migrations.AlterField(
            model_name='source',
            name='name',
            field=models.CharField(max_length=64, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='source',
            name='source_url',
            field=models.CharField(max_length=255, verbose_name='Source url'),
        ),
    ]
