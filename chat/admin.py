from django.contrib import admin

from chat.models import Task, Message
# Register your models here.

@admin.register(Task)
class TaskModelAdmin(admin.ModelAdmin):
    pass

@admin.register(Message)
class MessageModelAdmin(admin.ModelAdmin):
    list_display = ('id', '__str__')
