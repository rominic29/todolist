# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-17 14:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Priority',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TodoList',
            fields=[
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True)),
                ('order', models.AutoField(default=0, primary_key=True, serialize=False)),
                ('priority', models.ForeignKey(default='normal', on_delete=django.db.models.deletion.CASCADE, to='todoapp.Priority')),
                ('state', models.ForeignKey(default='pending', on_delete=django.db.models.deletion.CASCADE, to='todoapp.State')),
            ],
        ),
    ]