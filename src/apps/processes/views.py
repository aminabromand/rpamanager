from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, JsonResponse
from django.views.generic import DetailView, CreateView, UpdateView, ListView
from django.views.generic.base import View
from django.shortcuts import render, redirect, reverse

from apps.calcschemas.forms import UpdateCalcSchemaForm, CreateCalcSchemaForm

from .forms import UpdateServiceTaskForm, CreateServiceTaskForm
from .models import ServiceTask

# Create your views here.

class ServiceTaskListView(LoginRequiredMixin, ListView):
    model = ServiceTask
    template_name = 'processes/service_task_list.html'


class ServiceTaskView(View):
    def get_context_data(self, *args, **kwargs):
        context = super(ServiceTaskView, self).get_context_data(*args, **kwargs)
        qs = CalcSchema.objects.all()
        if qs.exists():
        	context['calc_schemas'] = qs
        return context


class UpdateServiceTaskView(LoginRequiredMixin, UpdateView):
    form_class = UpdateServiceTaskForm
    model = ServiceTask
    template_name = 'processes/service_task.html'

    def get_context_data(self, *args, **kwargs):
        context = super(UpdateServiceTaskView, self).get_context_data(*args, **kwargs)
        qs = ServiceTask.objects.all()
        if qs.exists():
            context['service_tasks'] = qs
        if self.object.calcschema:
            context['calc_schema_object'] = calc_schema
            calc_schema_form = UpdateCalcSchemaForm(self.object.calcschema)
            context['calc_schema_form'] = calc_schema_form
        else:
            calc_schema_form = CreateCalcSchemaForm()
            context['calc_schema_form'] = calc_schema_form
        return context


class CreateServiceTaskView(LoginRequiredMixin, CreateView):
    form_class = CreateServiceTaskForm
    model = ServiceTask
    template_name = 'processes/service_task.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CreateServiceTaskView, self).get_context_data(*args, **kwargs)
        qs = ServiceTask.objects.all()
        if qs.exists():
        	context['service_tasks'] = qs
        return context


@login_required
def update_service_task_save(request, pk):
	instance = ServiceTask.objects.get(pk=pk)
	form = UpdateServiceTaskForm(request.POST, instance=instance)
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
	return redirect('processes:update_service_task', pk=pk)


@login_required
def create_service_task_save(request):
	form = CreateServiceTaskForm(request.POST)
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
	return redirect('processes:update_service_task', pk=new_instance.pk)


@login_required
def delete_service_task(request, pk):
	instance = ServiceTask.objects.get(pk=pk).delete()
	if request.is_ajax():
		json_data = {
				"nextPath": reverse('processes:service_task_list'),
		}
		return JsonResponse(json_data)
	return redirect('processes:service_task_list')
