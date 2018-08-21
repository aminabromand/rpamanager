from django.db import models
from django.urls import reverse

from apps.applications.models import Application

# Create your models here.

class CalcSchema(models.Model):
	name 					    = models.CharField(max_length=120, unique=True)

	application					= models.ForeignKey(Application, on_delete=models.CASCADE)

	size_m				        = models.IntegerField(default=25)
	size_l		                = models.IntegerField(default=100)
	effort_factor_s			    = models.FloatField(default=1)
	effort_factor_m			    = models.FloatField(default=1.5)
	effort_factor_l			    = models.FloatField(default=3)

	panel_base_effort		    = models.IntegerField(default=0)
	panel_base_effort		    = models.IntegerField(default=0)
	input_field_base_effort	    = models.IntegerField(default=0)
	button_base_effort			= models.IntegerField(default=0)
	dropdown_base_effort		= models.IntegerField(default=0)
	checkbox_base_effort		= models.IntegerField(default=0)
	radio_button_base_effort    = models.IntegerField(default=0)
	file_input_base_effort	    = models.IntegerField(default=0)

	updated 				    = models.DateTimeField(auto_now=True)
	timestamp 				    = models.DateTimeField(auto_now_add=True)

	def get_absolute_url(self):
		return reverse('calcschemas:update_calc_schema', kwargs={'pk': self.pk})

	def __str__(self):
		return str(self.name)
