# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-19 04:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_manager', '0003_usertag_is_subscribed'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserTag',
            new_name='Subscription',
        ),
    ]