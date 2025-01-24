from django.urls import path
from .consumers import EchoConsumer

ws_urlpatterns = [
    path('ws/sc/', EchoConsumer.as_asgi()),
]