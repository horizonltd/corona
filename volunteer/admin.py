from django.contrib import admin
from . models import Volunteer, HighestQualification, Profession, State, Lga, Ward
# Register your models here.


# class DoctorAdmin(admin.ModelAdmin):
#     search_fields = ['__all__']

# class ExpertiseAdmin(admin.ModelAdmin):
#     search_fields = ['__all__']

class VolunteerAdmin(admin.ModelAdmin):
    search_fields = ['__all__']


class HighestQualificationAdmin(admin.ModelAdmin):
    search_fields = ['__all__']

class ProfessionAdmin(admin.ModelAdmin):
    search_fields = ['__all__']

class StateAdmin(admin.ModelAdmin):
    search_fields = ['__all__']


class LgaAdmin(admin.ModelAdmin):
    search_fields = ['__all__']

class WardAdmin(admin.ModelAdmin):
    search_fields = ['__all__']

admin.site.register(HighestQualification, HighestQualificationAdmin)
admin.site.register(Profession, ProfessionAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Lga, LgaAdmin)
admin.site.register(Ward, WardAdmin)
admin.site.register(Volunteer, VolunteerAdmin)
# admin.site.register(Expertise, ExpertiseAdmin)
# admin.site.register(Doctor, DoctorAdmin)


