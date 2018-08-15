from django.contrib import admin

from .models import Process, Application, ServiceTask

# Register your models here.

admin.site.register(Process)
admin.site.register(Application)
admin.site.register(ServiceTask)
