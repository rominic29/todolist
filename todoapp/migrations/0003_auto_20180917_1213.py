# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-09-17 15:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_auto_20180917_1108'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='State',
            new_name='Category',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='todolist',
            options={'ordering': ['-created']},
        ),
        migrations.RenameField(
            model_name='todolist',
            old_name='description',
            new_name='content',
        ),
        migrations.RemoveField(
            model_name='todolist',
            name='order',
        ),
        migrations.RemoveField(
            model_name='todolist',
            name='priority',
        ),
        migrations.RemoveField(
            model_name='todolist',
            name='state',
        ),
        migrations.AddField(
            model_name='todolist',
            name='category',
            field=models.ForeignKey(default='general', on_delete=django.db.models.deletion.CASCADE, to='todoapp.Category'),
        ),
        migrations.AddField(
            model_name='todolist',
            name='created',
            field=models.DateField(default='2018-09-17'),
        ),
        migrations.AddField(
            model_name='todolist',
            name='due_date',
            field=models.DateField(default='2018-09-17'),
        ),
        migrations.AddField(
            model_name='todolist',
            name='id',
            field=models.AutoField(auto_created=True, default=django.utils.timezone.now, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Priority',
        ),
    ]