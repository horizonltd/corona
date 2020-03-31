from django.contrib import admin
from . models import Doctor, Expertise
# Register your models here.


class DoctorAdmin(admin.ModelAdmin):
    search_fields = ['__all__']

class ExpertiseAdmin(admin.ModelAdmin):
    search_fields = ['__all__']

admin.site.register(Expertise, ExpertiseAdmin)
admin.site.register(Doctor, DoctorAdmin)

