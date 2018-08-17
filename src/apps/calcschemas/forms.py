from django import forms
from django.forms import ModelForm, NumberInput

from .models import CalcSchema


class UpdateCalcSchemaForm(forms.ModelForm):
    class Meta:
        model = CalcSchema
        fields = [
            'size_m',
            'size_l',
            'effort_factor_s',
            'effort_factor_m',
            'effort_factor_l',
            'panel_base_effort',
            'input_field_base_effort',
            'button_base_effort',
            'dropdown_base_effort',
            'checkbox_base_effort',
            'radio_button_base_effort',
            'file_input_base_effort',
        ]
        widgets = {
            'size_m': NumberInput(attrs={'class': 'numberbox'}),
            'size_l': NumberInput(attrs={'class': 'numberbox'}),
            'effort_factor_s': NumberInput(attrs={'class': 'numberbox'}),
            'effort_factor_m': NumberInput(attrs={'class': 'numberbox'}),
            'effort_factor_l': NumberInput(attrs={'class': 'numberbox'}),
        }


class CreateCalcSchemaForm(forms.ModelForm):
    class Meta:
        model = CalcSchema
        fields = [
            'name',
            'size_m',
            'size_l',
            'effort_factor_s',
            'effort_factor_m',
            'effort_factor_l',
            'panel_base_effort',
            'input_field_base_effort',
            'button_base_effort',
            'dropdown_base_effort',
            'checkbox_base_effort',
            'radio_button_base_effort',
            'file_input_base_effort',
        ]
        widgets = {
            'size_m': NumberInput(attrs={'class': 'numberbox'}),
            'size_l': NumberInput(attrs={'class': 'numberbox'}),
            'effort_factor_s': NumberInput(attrs={'class': 'numberbox'}),
            'effort_factor_m': NumberInput(attrs={'class': 'numberbox'}),
            'effort_factor_l': NumberInput(attrs={'class': 'numberbox'}),
        }
