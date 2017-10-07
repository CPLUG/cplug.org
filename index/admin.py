from django.contrib import admin
from adminsortable.admin import SortableAdmin
from .models import Event, Officer

# Register your models here.
admin.site.register(Event)
admin.site.register(Officer, SortableAdmin)
