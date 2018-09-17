# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-17 17:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0004_auto_20180917_1445'),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='todolist',
            name='priority',
            field=models.ForeignKey(default='normal', on_delete=django.db.models.deletion.CASCADE, to='todoapp.Priority'),
        ),
        migrations.AddField(
            model_name='todolist',
            name='status',
            field=models.ForeignKey(default='pending', on_delete=django.db.models.deletion.CASCADE, to='todoapp.Status'),
        ),
    ]
