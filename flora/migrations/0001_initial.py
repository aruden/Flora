# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-14 13:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('norwegain_name', models.CharField(max_length=100)),
                ('latin_name', models.CharField(blank=True, max_length=100)),
                ('english_name', models.CharField(blank=True, max_length=100)),
                ('norwegian_family', models.CharField(max_length=100)),
                ('latin_family', models.CharField(max_length=100)),
                ('english_family', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]