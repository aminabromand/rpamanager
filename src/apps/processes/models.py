from django.db import models
from django.urls import reverse

from apps.calcschemas.models import CalcSchema

# Create your models here.

class Process(models.Model):
	name			= models.CharField(max_length=120)
	description		= models.TextField()
	# customer		= models.ForeignKey(User, null=True, blank=True)

	updated 		= models.DateTimeField(auto_now=True)
	timestamp 		= models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return str(self.name)


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

	def __str__(self):
		return str(self.name)


SCHEDULE_TYPES = (
	('triggered', 'Event triggered'),
	('timely', 'Timely scheduled'),
)

class ServiceTask(models.Model):
	name 					= models.CharField(max_length=120, unique=True)
	description				= models.TextField()

	application				= models.ForeignKey(Application, null=True, blank=True, on_delete=models.CASCADE)
	processes				= models.ManyToManyField(Process, blank=True)
	calcschema				= models.ForeignKey(CalcSchema, null=True, blank=True, on_delete=models.SET_NULL)

	schedule_type			= models.CharField(max_length=20, choices=SCHEDULE_TYPES)
	exec_duration_man		= models.IntegerField(default=0)
	exec_duration_auto		= models.IntegerField(default=0)
	instance_count_monthly	= models.IntegerField(default=0)

	gateway_count			= models.IntegerField(default=0)

	panel_count				= models.IntegerField(default=0)
	input_field_count		= models.IntegerField(default=0)
	button_count			= models.IntegerField(default=0)
	dropdown_count			= models.IntegerField(default=0)
	checkbox_count			= models.IntegerField(default=0)
	radio_button_count		= models.IntegerField(default=0)
	file_input_count		= models.IntegerField(default=0)

	updated 				= models.DateTimeField(auto_now=True)
	timestamp 				= models.DateTimeField(auto_now_add=True)

	def get_absolute_url(self):
		return reverse('processes:update_service_task', kwargs={'pk': self.pk})

	def __str__(self):
		return str(self.name)
