# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-17 14:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='todolist',
            options={'ordering': ['order']},
        ),
    ]