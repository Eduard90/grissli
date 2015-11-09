from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^chat/api/bot/command/(?P<task_id>\d+)/$', 'chat.views.api_bot_task', name='api-bot-task'),
    url(r'^chat/api/bot/command/$', 'chat.views.api_bot_command', name='api-bot-command'),
    url(r'^chat/api/message/$', 'chat.views.api_message', name='api-message'),
    url(r'^chat/api/login/$', 'chat.views.api_login', name='api-login'),
    url(r'$', 'chat.views.index', name='chat-index'),
)
