# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-23 18:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TODO_List', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo_item',
            name='description',
            field=models.TextField(max_length=500, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='todo_item',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
    ]