"""
ASGI config for covid19_project project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "covid19_project.settings")

application = get_asgi_application()
import realtimedataload.routing

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket":URLRouter(
                realtimedataload.routing.websocket_urlpatterns
            )
        # Just HTTP for now. (We can add other protocols later.)
    }
)
app = application

