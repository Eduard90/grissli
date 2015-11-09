# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_auto_20151109_1746'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['id']},
        ),
    ]
