from django import forms
from django.forms import ModelForm, Textarea

from .models import Application


class UpdateApplicationForm(forms.ModelForm):
	class Meta:
		model = Application
		fields = [
			'description',

			'app_type',
			'has_interface',
		]
		widgets = {
			'description': Textarea(attrs={'cols': 20, 'rows': 3}),
		}


class CreateApplicationForm(forms.ModelForm):
	class Meta:
		model = Application
		fields = [
			'name',
			'description',

			'app_type',
			'has_interface',
		]
		widgets = {
			'description': Textarea(attrs={'cols': 20, 'rows': 3}),
		}
