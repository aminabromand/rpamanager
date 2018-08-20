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


@login_required
def get_calc_schema(request):
    pk = request.POST.get('calc_schema_id', None)
    if pk:
        instance = CalcSchema.objects.get(pk=pk)
        if instance:
            json_data = {
                'id': instance.pk,
                'name': instance.name,
                'size_m': instance.size_m,
                'size_l': instance.size_l,
                'effort_factor_s': instance.effort_factor_s,
                'effort_factor_m': instance.effort_factor_m,
                'effort_factor_l': instance.effort_factor_l,

                'panel_base_effort': instance.panel_base_effort,
                'panel_base_effort': instance.panel_base_effort,
                'input_field_base_effort': instance.input_field_base_effort,
                'button_base_effort': instance.button_base_effort,
                'dropdown_base_effort': instance.dropdown_base_effort,
                'checkbox_base_effort': instance.checkbox_base_effort,
                'radio_button_base_effort': instance.radio_button_base_effort,
                'file_input_base_effort': instance.file_input_base_effort,
            }
            return JsonResponse(json_data)
    json_data = {
        'msg': 'Not found.'
    }
    return JsonResponse(json_data)


@login_required
def save_calc_schema(request, pk=None):
    instance = None
    if pk:
        instance = CalcSchema.objects.get(pk=pk)
        print(request.POST.get("name"))
        form = UpdateCalcSchemaForm(request.POST, instance=instance)
    else:
        form = CreateCalcSchemaForm(request.POST)
    form_saved = False
    msg = 'error'
    if form.is_valid():
        instance = form.save()
        instance_id = instance.id
        form_saved = True
        msg = 'task saved'
    else:
        #error_list = "errors: "
        error_list = []
        for error in form.errors:
            error_list.append(str(error) + ': ' + str(form.errors[error]))
        msg = str(form.errors)
        instance_id = None
    if request.is_ajax():
        json_data = {
                "msg": msg,
                'id': instance_id,
        }
        return JsonResponse(json_data)
    return redirect('processes:update_service_task', pk=instance.pk)


# @login_required
# def update_calc_schema_save(request, pk):
#     instance = CalcSchema.objects.get(pk=pk)
#     form = UpdateCalcSchemaForm(request.POST, instance=instance)
#     form_saved = False
#     msg = 'error'
#     if form.is_valid():
#         form.save();
#         form_saved = True
#         msg = 'task saved'
#     if request.is_ajax():
#         json_data = {
#                 "msg": msg,
#         }
#         return JsonResponse(json_data)
#     return redirect('calcschemas:update_calc_schema', pk=pk)


# @login_required
# def create_calc_schema_save(request):
#     form = CreateCalcSchemaForm(request.POST)
#     form_saved = False
#     msg = 'error'
#     new_instance = None
#     if form.is_valid():
#         form.save();
#         new_instance = form_saved = True
#         msg = 'task saved'
#     if request.is_ajax():
#         json_data = {
#                 "msg": msg,
#         }
#         return JsonResponse(json_data)
#     return redirect('calcschemas:update_calc_schema', pk=new_instance.pk)


@login_required
def delete_calc_schema(request, pk):
    instance = CalcSchema.objects.get(pk=pk).delete()
    if request.is_ajax():
        json_data = {
                "nextPath": reverse('calcschemas:calc_schema_list'),
        }
        return JsonResponse(json_data)
    return redirect('calcschemas:calc_schema_list')
