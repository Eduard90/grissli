# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_auto_20151109_1757'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения', 'ordering': ['id']},
        ),
        migrations.AlterModelOptions(
            name='task',
            options={'verbose_name': 'Задача', 'verbose_name_plural': 'Задачи'},
        ),
        migrations.AlterField(
            model_name='task',
            name='task',
            field=models.CharField(choices=[('GET_TITLE', 'Получить заголовок'), ('GET_TITLES', 'Получить заголовки'), ('GET_H1', 'Получить H1'), ('REMIND', 'Напомнить')], verbose_name='Задача', max_length=20, default=''),
        ),
    ]
