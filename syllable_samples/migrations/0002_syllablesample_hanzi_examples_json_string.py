# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-19 18:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('syllable_samples', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='syllablesample',
            name='hanzi_examples_json_string',
            field=models.CharField(default='{}', max_length=80),
        ),
    ]
