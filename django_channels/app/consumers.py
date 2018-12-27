from .models import *
from channels.consumer import SyncConsumer, AsyncConsumer
from channels.db import database_sync_to_async
import os

class updateCustomerConsumer(AsyncConsumer):
	async def performUpdates(self, data):
		customers = Customer.objects.all()
		for customer in customers:
			customer.updateCustomer()

