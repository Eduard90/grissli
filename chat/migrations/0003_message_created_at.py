# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2015, 11, 9, 15, 58, 55, 37494, tzinfo=utc), verbose_name='Создано', auto_now_add=True),
            preserve_default=False,
        ),
    ]
