from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, JsonResponse
from django.views.generic import DetailView, CreateView, UpdateView, ListView, View
from django.shortcuts import render, redirect, reverse

from .forms import UpdateApplicationForm, CreateApplicationForm
from .models import Application

# Create your views here.

class ApplicationListView(LoginRequiredMixin, ListView):
    model = Application
    template_name = 'applications/application_list.html'


class ApplicationView(LoginRequiredMixin, View):
    model = Application
    template_name = 'applications/application.html'

    def get_context_data(self, *args, **kwargs):
        context = super(ApplicationView, self).get_context_data(*args, **kwargs)
        qs = Application.objects.all()
        if qs.exists():
        	context['applications'] = qs
        return context


class UpdateApplicationView(ApplicationView, UpdateView):
    form_class = UpdateApplicationForm


class CreateApplicationView(ApplicationView, CreateView):
    form_class = CreateApplicationForm


@login_required
def save_application(request, pk=None):
    instance = None
    if pk:
        instance = Application.objects.get(pk=pk)
        form = UpdateApplicationForm(request.POST, instance=instance)
    else:
        form = CreateApplicationForm(request.POST)
    form_saved = False
    msg = 'error'
    if form.is_valid():
        instance = form.save()
        form_saved = True
        msg = 'application saved'
    if request.is_ajax():
        json_data = {
                "msg": msg,
        }
        return JsonResponse(json_data)
    return redirect('applications:update_application', pk=instance.pk)


@login_required
def delete_application(request, pk):
    instance = Application.objects.get(pk=pk).delete()
    if request.is_ajax():
        json_data = {
                "nextPath": reverse('applications:application_list'),
        }
        return JsonResponse(json_data)
    return redirect('processes:application_list')
