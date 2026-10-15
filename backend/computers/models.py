from django.db import models


class Computer(models.Model):
	class Status(models.TextChoices):
		ONLINE = 'Online', 'Online'
		OFFLINE = 'Offline', 'Offline'

	pc_name = models.CharField(max_length=100, unique=True)
	ip_address = models.GenericIPAddressField(unique=True)
	status = models.CharField(max_length=10, choices=Status.choices, default=Status.OFFLINE)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	class Meta:
		ordering = ['pc_name']

	def __str__(self):
		return self.pc_name

# Create your models here.
