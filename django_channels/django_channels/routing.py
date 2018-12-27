from channels.routing import ProtocolTypeRouter, URLRouter, ChannelNameRouter
from channels.auth import AuthMiddlewareStack
from channels.security.websocket import AllowedHostsOriginValidator, OriginValidator

from app.consumers import *

application = ProtocolTypeRouter({
	'channel':ChannelNameRouter({
        'updateCustomerRoute':updateCustomerConsumer
        })
})


