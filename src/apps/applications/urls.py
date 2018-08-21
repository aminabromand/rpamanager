from django.conf.urls import url

from .views import (
	ApplicationListView,
    UpdateApplicationView,
    CreateApplicationView,
    delete_application,
    save_application,
    )

app_name='applications'
urlpatterns = [
	url(r'^update/(?P<pk>[\w-]+)/save/$', save_application, name='update_application-save'),
	url(r'^update/(?P<pk>[\w-]+)/delete/$', delete_application, name='delete_application'),
    url(r'^update/(?P<pk>[\w-]+)/$', UpdateApplicationView.as_view(), name='update_application'),
	url(r'^create/save/$', save_application, name='create_application-save'),
	url(r'^create/$', CreateApplicationView.as_view(), name='create_application'),
	url(r'^$', ApplicationListView.as_view(), name='application_list'),
]
