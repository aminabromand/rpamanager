from django.conf.urls import url

from .views import (
	CalcSchemaListView,
    UpdateCalcSchemaView,
    CreateCalcSchemaView,
    save_calc_schema,
    delete_calc_schema,
    )

app_name='calcschemas'
urlpatterns = [
	url(r'^update/(?P<pk>[\w-]+)/save/$', save_calc_schema, name='update_calc_schema-save'),
	url(r'^update/(?P<pk>[\w-]+)/delete/$', delete_calc_schema, name='delete_calc_schema'),
    url(r'^update/(?P<pk>[\w-]+)/$', UpdateCalcSchemaView.as_view(), name='update_calc_schema'),
	url(r'^create/save/$', save_calc_schema, name='create_calc_schema-save'),
	url(r'^create/$', CreateCalcSchemaView.as_view(), name='create_calc_schema'),
	url(r'^$', CalcSchemaListView.as_view(), name='calc_schema_list'),
]
