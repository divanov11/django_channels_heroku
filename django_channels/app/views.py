from django.shortcuts import render
from .models import *
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync

def index(request):
	#Must specify type. Type is the consumers function
	data = {
	'type':'performUpdates'
	
	}
	channel_layer = get_channel_layer()
	async_to_sync(channel_layer.send)('updateCustomerRoute', data)

	return render(request, 'app/index.html')
