# Generated by Django 4.2.2 on 2023-07-04 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_collection_added_on'),
    ]

    operations = [
        migrations.AddField(
            model_name='collection',
            name='bio',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
    ]