# Generated by Django 4.2.2 on 2023-07-04 20:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_collection'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='added_on',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
