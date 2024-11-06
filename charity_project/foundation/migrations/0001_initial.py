# Generated by Django 5.1 on 2024-11-06 10:12

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('full_description', models.TextField(default='Описание отсутствует')),
                ('image', models.ImageField(upload_to='events/')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('location', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SuccessStory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='success_stories/')),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
    ]
