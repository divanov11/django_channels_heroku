from django.db import models
import time


class Customer(models.Model):
	name = models.CharField(max_length=200, blank=True, null=True)
	status = models.BooleanField(default=True)

	def __str__(self):
		return self.name

	def updateCustomer(self):

		if self.status == True:
			self.status = False
		else:
			self.status = True

		self.save()
		time.sleep(2) 

		print(str(self.name) + ': Status updated to ' + str(self.status))
		return None


