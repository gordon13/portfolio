# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 01:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_auto_20160128_0120'),
    ]

    operations = [
        migrations.AddField(
            model_name='software',
            name='sType',
            field=models.CharField(blank=True, choices=[(b'art', b'Art'), (b'tool', b'Tool'), (b'misc', b'Misc')], max_length=50, null=True),
        ),
    ]
