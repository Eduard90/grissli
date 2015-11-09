import time
import json
import datetime

from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers

from chat.bot import Bot
from chat.models import Task, Message
# Create your views here.

def index(request):
    return render(request, template_name='chat/index.html')

def api_bot_command(request):
    command_str = request.GET.get('command', False)
    res = Bot.parse_command_string(command_str)
    # res = Bot.parse_command_string("Бот, дай мне заголовок сайта http://ya.ru")
    # res = Bot.parse_command_string("Бот, напомни мне ололо через 5")
    cur_date = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    messages = []
    # If command not recognized
    if res is False:
        # Messages for send to client
        user_message = {'time': cur_date, 'nick': request.session['nick'], 'text': command_str}
        bot_message = {'time': cur_date, 'nick': 'Bot', 'text': 'Команда не распознана'}
        messages.append(user_message)
        messages.append(bot_message)
        # Store messages ...
        Message.from_messages(messages)
        return JsonResponse({'task_id': 0, 'error': 'Incorrect command', 'messages': messages})
    else:
        # Right command
        task_str = getattr(Task, 'TASK_{0}'.format(res['command']))
        task = Task()
        task.task = task_str
        task.args = json.dumps(res['args'])
        task.save()

        # Messages for send to client
        user_message = {'time': cur_date, 'nick': request.session['nick'], 'text': command_str}
        bot_message = {'time': cur_date, 'nick': 'Bot', 'text': 'Команда {0} успешно добавлена'.format(res['command'])}
        messages.append(user_message)
        messages.append(bot_message)
        # Store messages ...
        Message.from_messages(messages)
        return JsonResponse({'task_id': task.pk, 'task': res['command'], 'messages': messages})


def api_bot_task(request, task_id):
    messages = []
    try:
        task = Task.objects.get(pk=task_id)
        task.status = Task.TASK_STATUS_PROCESS
        task.save()
        task_command = task.task
        args = json.loads(task.args)

        # For REMIND command we need additional argument: timestamp when task created
        if task_command == 'REMIND':
            args.append(time.mktime(task.created_at.timetuple()))

        result = Bot.run_command(task_command, args)
        task.status = Task.TASK_STATUS_COMPLETE
        task.result = json.dumps(result)
        task.save()
        cur_date = datetime.datetime.now().strftime('%d.%m.%Y %H:%M:%S')
        # Message for send to client
        bot_message = {
            'time': cur_date, 'nick': 'Bot',
            'text': 'Результат выполнения команды {0}: {1}'.format(task_command, result)
        }
        if task_command == 'REMIND':
            bot_message['text'] = 'Напоминаю: {0}'.format(result)

        messages.append(bot_message)
        if result != -1:
            # Store messages ...
            Message.from_messages(messages)
        return JsonResponse({'result': result, 'messages': messages})
    except Task.DoesNotExist:
        return JsonResponse({'result': 0, 'error': 'Incorrect task_id'})


def api_message(request):
    # Greeting message
    message = Message()
    message.nick = 'Bot'
    message.text = 'Привет, {0}!'.format(request.session['nick'])
    message.save()

    messages = Message.objects.all()
    messages_format = []
    # Some operations ... Reformat data (for frontend)
    for message in messages:
        message_format = {
            'time': message.created_at.strftime('%d.%m.%Y %H:%M:%S'),
            'nick': message.nick,
            'text': message.text,
        }
        messages_format.append(message_format)

    return JsonResponse({'messages': messages_format})

def api_login(request):
    nick = request.GET.get('nick', '')
    if len(nick) > 2:
        request.session['nick'] = nick
        return JsonResponse({'result': 1})
    else:
        return JsonResponse({'result': 'Error! Nick is very short :('})