from django.contrib import admin

from .models import Collection, Task

admin.site.register(Collection)
admin.site.register(Task)