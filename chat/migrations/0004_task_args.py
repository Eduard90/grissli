# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_message_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='args',
            field=models.CharField(max_length=250, default='', verbose_name='Аргументы'),
        ),
    ]
