# Generated by Django 3.0.4 on 2020-03-27 20:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinic', '0014_auto_20200327_0206'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='verification_problem',
            field=models.PositiveIntegerField(choices=[(0, 'N/A'), (1, 'Submitted a resume or CV'), (2, 'Submitted an unacceptable credential'), (3, 'Fake or malicious submission'), (4, 'Other')], default=0),
        ),
    ]
