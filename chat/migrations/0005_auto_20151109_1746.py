# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_task_args'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='nick',
            field=models.CharField(verbose_name='Ник', default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='task',
            name='args',
            field=models.CharField(verbose_name='Аргументы', default='{}', max_length=250),
        ),
        migrations.AlterField(
            model_name='task',
            name='task',
            field=models.CharField(verbose_name='Задача', default='', max_length=20, choices=[('GET_TITLE', 'Получить заголовок'), ('GET_H1', 'Получить H1'), ('REMIND', 'Напомнить')]),
        ),
    ]
