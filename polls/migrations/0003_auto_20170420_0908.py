# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-20 09:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20170420_0901'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='news_Article_Heading',
            new_name='question_text',
        ),
    ]
