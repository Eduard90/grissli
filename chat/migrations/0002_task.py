# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('task', models.CharField(choices=[('GET_TITLE', 'Получить заголовок')], max_length=20, default='', verbose_name='Задача')),
                ('status', models.CharField(choices=[('CREATED', 'Создана'), ('PROCESS', 'В процессе'), ('COMPLETE', 'Завершена')], max_length=20, default='CREATED', verbose_name='Статус')),
                ('result', models.TextField(default='{}', verbose_name='Результат')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Создана')),
            ],
        ),
    ]
