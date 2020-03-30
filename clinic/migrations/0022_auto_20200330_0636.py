# Generated by Django 3.0.4 on 2020-03-30 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0021_auto_20200329_1836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='verified',
            field=models.BooleanField(default=False, help_text='Allows the provider to receive calls. Approving a provider will trigger an email to be sent to them.', verbose_name='approved'),
        ),
    ]
