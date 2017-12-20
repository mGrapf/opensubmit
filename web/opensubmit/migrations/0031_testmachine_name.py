# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-15 18:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('opensubmit', '0030_testmachine_enabled'),
    ]

    operations = [
        migrations.AddField(
            model_name='testmachine',
            name='name',
            field=models.CharField(help_text='Human-readable name of this machine.', max_length=50, null=True),
        ),
    ]
