# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-20 02:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20170519_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.ManyToManyField(related_name='category', to='blog.Category'),
        ),
    ]
