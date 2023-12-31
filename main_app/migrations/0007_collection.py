# Generated by Django 4.2.2 on 2023-07-04 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0006_crystal'),
    ]

    operations = [
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('crystals', models.ManyToManyField(to='main_app.crystal')),
            ],
            options={
                'verbose_name': 'collection',
                'verbose_name_plural': 'collections',
            },
        ),
    ]
