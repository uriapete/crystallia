# Generated by Django 4.2.2 on 2023-07-03 22:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_alter_crystaltype_bio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Crystal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.CharField(blank=True, max_length=5000, null=True)),
                ('summary', models.TextField(blank=True, max_length=5000, null=True)),
                ('color', models.CharField(blank=True, max_length=250, null=True)),
                ('mohs_hardness', models.DecimalField(blank=True, decimal_places=2, max_digits=3, null=True)),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('found_on', models.DateField(blank=True, null=True)),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='crystal', to='main_app.crystaltype')),
            ],
            options={
                'verbose_name': 'crystal',
                'verbose_name_plural': 'crystals',
            },
        ),
    ]