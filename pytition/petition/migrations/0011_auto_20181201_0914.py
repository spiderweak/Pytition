# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-12-01 08:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0010_permission_can_modify_permissions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pytitionuser',
            old_name='permission',
            new_name='permissions',
        ),
    ]
