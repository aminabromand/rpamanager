from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, JsonResponse
from django.views.generic import DetailView, CreateView, UpdateView, ListView
from django.views.generic.base import View
from django.shortcuts import render, redirect, reverse

from apps.calcschemas.forms import UpdateCalcSchemaForm, CreateCalcSchemaForm
from apps.calcschemas.models import CalcSchema

from .forms import UpdateServiceTaskForm, CreateServiceTaskForm
from .models import ServiceTask

# Create your views here.

class ServiceTaskListView(LoginRequiredMixin, ListView):
    model = ServiceTask
    template_name = 'processes/service_task_list.html'


class ServiceTaskView(LoginRequiredMixin, View):
    calc_schemas = None
    def get_context_data(self, *args, **kwargs):
        context = super(ServiceTaskView, self).get_context_data(*args, **kwargs)
        qs = CalcSchema.objects.all()
        if qs.exists():
            self.calc_schemas = qs
            context['calc_schemas'] = qs
        return context


class UpdateServiceTaskView(ServiceTaskView, UpdateView):
    form_class = UpdateServiceTaskForm
    model = ServiceTask
    template_name = 'processes/service_task.html'

    def get_context_data(self, *args, **kwargs):
        context = super(UpdateServiceTaskView, self).get_context_data(*args, **kwargs)
        qs = ServiceTask.objects.all()

        if self.calc_schemas:
            self.calc_schemas = self.calc_schemas.filter(application=self.object.application)
            context['calc_schemas'] = self.calc_schemas

        if qs.exists():
            context['service_tasks'] = qs

        if self.object.calcschema:
            context['calc_schema_object'] = self.object.calcschema
            calc_schema_form = UpdateCalcSchemaForm(instance=self.object.calcschema)
            context['calc_schema_form'] = calc_schema_form
        else:
            calc_schema_form = CreateCalcSchemaForm()
            context['calc_schema_form'] = calc_schema_form

        return context


class CreateServiceTaskView(ServiceTaskView, CreateView):
    form_class = CreateServiceTaskForm
    model = ServiceTask
    template_name = 'processes/service_task.html'

    def get_context_data(self, *args, **kwargs):
        context = super(CreateServiceTaskView, self).get_context_data(*args, **kwargs)
        qs = ServiceTask.objects.all()
        if qs.exists():
        	context['service_tasks'] = qs
        calc_schema_form = CreateCalcSchemaForm()
        context['calc_schema_form'] = calc_schema_form
        return context


@login_required
def save_service_task(request, pk=None):
    instance = None
    if pk:
        instance = ServiceTask.objects.get(pk=pk)
        form = UpdateServiceTaskForm(request.POST, instance=instance)
    else:
        form = CreateServiceTaskForm(request.POST)
    form_saved = False
    msg = 'error'
    if form.is_valid():
        instance = form.save(commit=False)

        calc_schema_id = request.POST.get("reference", None)
        if calc_schema_id:
            calc_schema_instance = CalcSchema.objects.get(pk=calc_schema_id)
            instance.calcschema = calc_schema_instance
        instance.save()
        form.save_m2m()
        form_saved = True
        msg = 'task saved'
    if request.is_ajax():
        json_data = {
                "msg": msg,
        }
        return JsonResponse(json_data)
    return redirect('processes:update_service_task', pk=instance.pk)


@login_required
def delete_service_task(request, pk):
    instance = ServiceTask.objects.get(pk=pk).delete()
    if request.is_ajax():
        json_data = {
                "nextPath": reverse('processes:service_task_list'),
        }
        return JsonResponse(json_data)
    return redirect('processes:service_task_list')
