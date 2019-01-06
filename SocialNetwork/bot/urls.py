from django.urls import path, include
from rest_framework import routers

from bot.views import bot_start_view

urlpatterns = [
    path('bot/start', bot_start_view),
]
