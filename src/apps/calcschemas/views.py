from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, JsonResponse
from django.views.generic import DetailView, CreateView, UpdateView, ListView
from django.shortcuts import render, redirect, reverse

from .forms import UpdateCalcSchemaForm, CreateCalcSchemaForm
from .models import CalcSchema


# Create your views here.

class CalcSchemaListView(LoginRequiredMixin, ListView):
    model = CalcSchema
    template_name = 'calcschemas/calc_schema_list.html'


class UpdateCalcSchemaView(LoginRequiredMixin, UpdateView):
    form_class = UpdateCalcSchemaForm
    model = CalcSchema
    template_name = 'calcschemas/calc_schema.html'

    def get_context_data(self, *args, **kwargs):
        context = super(UpdateCalcSchemaView, self).get_context_data(*args, **kwargs)
        qs = CalcSchema.objects.all()
        if qs.exists():
        	context['calc_schemas'] = qs
        return context


@login_required
def update_calc_schema_save(request, pk):
	instance = CalcSchema.objects.get(pk=pk)
	form = UpdateCalcSchemaForm(request.POST, instance=instance)
	form_saved = False
	msg = 'error'
	if form.is_valid():
		form.save();
		form_saved = True
		msg = 'task saved'
	if request.is_ajax():
		json_data = {
				"msg": msg,
		}
		return JsonResponse(json_data)
	return redirect('calcschemas:update_calc_schema', pk=pk)


@login_required
def create_calc_schema_save(request):
	form = CreateCalcSchemaForm(request.POST)
	form_saved = False
	msg = 'error'
	new_instance = None
	if form.is_valid():
		form.save();
		new_instance = form_saved = True
		msg = 'task saved'
	if request.is_ajax():
		json_data = {
				"msg": msg,
		}
		return JsonResponse(json_data)
	return redirect('calcschemas:update_calc_schema', pk=new_instance.pk)


@login_required
def delete_calc_schema(request, pk):
	instance = CalcSchema.objects.get(pk=pk).delete()
	if request.is_ajax():
		json_data = {
				"nextPath": reverse('calcschemas:calc_schema_list'),
		}
		return JsonResponse(json_data)
	return redirect('calcschemas:calc_schema_list')


class CreateCalcSchemaView(LoginRequiredMixin, CreateView):
    form_class = CreateCalcSchemaForm
    model = CalcSchema
    template_name = 'calcschemas/calc_schema.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CreateCalcSchemaView, self).get_context_data(*args, **kwargs)
        qs = CalcSchema.objects.all()
        if qs.exists():
        	context['calc_schemas'] = qs
        return context
