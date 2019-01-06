from rest_framework.decorators import api_view
from rest_framework.response import Response
from zappa.async import task

from bot.auto_bot import AutoBot


@task
def bot_start():
    try:
        bot = AutoBot()
        bot.start()
    except SystemExit:
        pass


@api_view()
def bot_start_view(request):
    bot_start()
    return Response({
        'bot':
        'Automate Bot started in async mode.Please see result in admin panel. :)'
    })
