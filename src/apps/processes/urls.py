from django.conf.urls import url

from .views import (
	ServiceTaskListView,
    UpdateServiceTaskView,
    CreateServiceTaskView,
    update_service_task_save,
    create_service_task_save,
    delete_service_task,
    )

app_name='processes'
urlpatterns = [
	url(r'^update/(?P<pk>[\w-]+)/save/$', update_service_task_save, name='update_service_task-save'),
	url(r'^update/(?P<pk>[\w-]+)/delete/$', delete_service_task, name='delete_service_task'),
    url(r'^update/(?P<pk>[\w-]+)/$', UpdateServiceTaskView.as_view(), name='update_service_task'),
	url(r'^create/save/$', create_service_task_save, name='create_service_task-save'),
	url(r'^create/$', CreateServiceTaskView.as_view(), name='create_service_task'),
	url(r'^$', ServiceTaskListView.as_view(), name='service_task_list'),
]
