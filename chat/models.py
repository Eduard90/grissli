from django.db import models

# Create your models here.
class Message(models.Model):
    nick = models.CharField("Ник", max_length=50, default='')
    text = models.CharField("Текст", max_length=250, default='')
    created_at = models.DateTimeField("Создано", auto_now_add=True)

    class Meta:
        ordering = ['id']
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return "{0} {1}: {2}".format(self.created_at, self.nick, self.text)

    @staticmethod
    def from_messages(messages):
        for message in messages:
            msg = Message()
            msg.nick = message['nick']
            msg.text = message['text']
            msg.save()


class Task(models.Model):
    TASK_GET_TITLE = 'GET_TITLE'
    TASK_GET_TITLES = 'GET_TITLES'
    TASK_GET_H1 = 'GET_H1'
    TASK_REMIND = 'REMIND'
    TASKS_LIST = (
        (TASK_GET_TITLE, 'Получить заголовок'),
        (TASK_GET_TITLES, 'Получить заголовки'),
        (TASK_GET_H1, 'Получить H1'),
        (TASK_REMIND, 'Напомнить'),
    )

    TASK_STATUS_CREATED = 'CREATED'
    TASK_STATUS_PROCESS = 'PROCESS'
    TASK_STATUS_COMPLETE = 'COMPLETE'
    TASK_STATUS_LIST = (
        (TASK_STATUS_CREATED, 'Создана'),
        (TASK_STATUS_PROCESS, 'В процессе'),
        (TASK_STATUS_COMPLETE, 'Завершена'),
    )

    task = models.CharField("Задача", choices=TASKS_LIST, default='', max_length=20)
    args = models.CharField("Аргументы", default='{}', max_length=250)
    status = models.CharField("Статус", choices=TASK_STATUS_LIST, default=TASK_STATUS_CREATED, max_length=20)
    result = models.TextField("Результат", default="{}")
    created_at = models.DateTimeField("Создана", auto_now_add=True)

    class Meta:
        verbose_name = "Задача"
        verbose_name_plural = "Задачи"

    def __str__(self):
        return self.task