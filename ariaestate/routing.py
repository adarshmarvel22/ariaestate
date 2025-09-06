from django.conf.urls import url

from channels.routing import ChannelNameRouter, ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack

from ariaestate.consumers import ariaestate_WebSocketConsumer

# Consumer Imports
from ecommerce.consumers import ecommerceConsumer
from forum.consumers import forumConsumer
from properties.consumers import propertiesConsumer
from research.consumers import researchConsumer
from accounts.consumers import accountsConsumer


application = ProtocolTypeRouter({

    # WebSocket handler
    "websocket": AuthMiddlewareStack(
        URLRouter([
            url(r"^ws/$", ariaestate_WebSocketConsumer.as_asgi()),
        ])
    ),
    "channel": ChannelNameRouter({
        "ecommerce": ecommerceConsumer,    "forum": forumConsumer,    "properties": propertiesConsumer,    "research": researchConsumer,    "accounts": accountsConsumer,
    })
})
