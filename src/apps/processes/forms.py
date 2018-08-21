from django import forms
from django.forms import ModelForm, Textarea

from .models import ServiceTask


class UpdateServiceTaskForm(forms.ModelForm):
	class Meta:
		model = ServiceTask
		fields = [
			'description',
			# 'application',
			# 'processes',
			'schedule_type',
			'exec_duration_man',
			'exec_duration_auto',
			'instance_count_monthly',
			'panel_count',
			'input_field_count',
			'button_count',
			'dropdown_count',
			'checkbox_count',
			'radio_button_count',
			'file_input_count',
			'gateway_count',
		]
		widgets = {
			'description': Textarea(attrs={'cols': 20, 'rows': 3}),
		}


class CreateServiceTaskForm(forms.ModelForm):
	class Meta:
		model = ServiceTask
		fields = [
			'name',
			'description',
			'application',
			# 'processes',
			'schedule_type',
			'exec_duration_man',
			'exec_duration_auto',
			'instance_count_monthly',
			'panel_count',
			'input_field_count',
			'button_count',
			'dropdown_count',
			'checkbox_count',
			'radio_button_count',
			'file_input_count',
			'gateway_count',
		]
		widgets = {
			'description': Textarea(attrs={'cols': 20, 'rows': 3}),
		}
