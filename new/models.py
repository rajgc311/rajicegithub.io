from django.db import models

# Create your models here.
class Booking(models.Model):
	name = models.CharField(max_length=122)
	address = models.CharField(max_length=122)
	types = models.CharField(max_length=122)
	quantity = models.CharField(max_length=122)
	location = models.CharField(max_length=122)
	description = models.TextField()

	def __str__(self):
		return self.name

