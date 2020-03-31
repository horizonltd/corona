from django.contrib import admin
from .models import Appointment, Material


@admin.register(Appointment)
class AppoinmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'phone', 'doctor', 'date', 'time']
    date_hierarchy = ('date')
    list_filter = ['date', 'doctor', ]
    list_per_page = 20
    search_fields = ['doctor', 'name', ]


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'author', 'material', 'date']
    date_hierarchy = ('date')
    list_filter = ['date', 'title', ]
    list_per_page = 20
    search_fields = ['title', 'description', ]
