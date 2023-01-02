# chat/routing.py
from django.urls import path

from .consumers import ChatConsumer

websocket_urlpatterns = [
    path("r1/",ChatConsumer.as_asgi()),
]