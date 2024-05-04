import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
import src.apps.chat.routing
from src.apps.chat.middleware import TokenAuthMiddleware
from channels.security.websocket import AllowedHostsOriginValidator

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "src.settings")

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": TokenAuthMiddleware(
            AllowedHostsOriginValidator(
                URLRouter(src.apps.chat.routing.websocket_urlpatterns)
            )
        ),
    }
)
