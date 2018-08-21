from django.conf.urls import url

from .views import (
	logout_view,
    )

app_name='accounts'
urlpatterns = [
	url(r'^logout/$', logout_view, name='logout'),
]
