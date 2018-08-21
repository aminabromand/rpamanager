from django.db import models
from django.urls import reverse

# Create your models here.

APP_TYPES = (
	('fat', 'Fat Client'),
	('web', 'Web Client'),
)

class Application(models.Model):
	name			= models.CharField(max_length=120)
	description		= models.TextField()
	app_type		= models.CharField(max_length=20, choices=APP_TYPES)
	has_interface	= models.BooleanField(default=False)

	updated 		= models.DateTimeField(auto_now=True)
	timestamp 		= models.DateTimeField(auto_now_add=True)

	def get_absolute_url(self):
		return reverse('applications:update_application', kwargs={'pk': self.pk})

	def __str__(self):
		return str(self.name)
