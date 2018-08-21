from django.contrib import admin

from .models import Process, ServiceTask

# Register your models here.

admin.site.register(Process)
admin.site.register(ServiceTask)
