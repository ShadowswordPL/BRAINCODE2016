# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-19 01:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0002_auto_20160319_0114'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('img', models.ImageField(upload_to='files/')),
                ('students', models.ManyToManyField(to='backend.Student')),
            ],
        ),
    ]
