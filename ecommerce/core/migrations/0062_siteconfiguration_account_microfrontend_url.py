# Generated by Django 2.2.17 on 2020-11-13 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0061_auto_20200407_1725'),
    ]

    operations = [
        migrations.AddField(
            model_name='siteconfiguration',
            name='account_microfrontend_url',
            field=models.URLField(blank=True, help_text='URL for the Account Microfrontend (used to lead learners to ID verification workflow)', null=True, verbose_name='Account Microfrontend URL'),
        ),
    ]
