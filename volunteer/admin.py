from django.contrib import admin
from . models import Volunteer, Qualification, Profession, State, Lga, Ward, Specialization, ReportCase


@admin.register(ReportCase)
class ReportCaseAdmin(admin.ModelAdmin):
    list_display = ['first_Name', 'middle_Name', 'state', 'lga', 'ward','reportDate']
    date_hierarchy = ('reportDate')
    list_filter = ['first_Name', 'state', ]
    list_per_page = 20
    search_fields = ['first_Name', 'reportDate','lga']


@admin.register(Volunteer)
class VolunteerAdmin(admin.ModelAdmin):
    list_display = ['first_Name', 'middle_Name', 'state', 'lga', 'ward','prepared_Start_DateTobeInvolved','prepared_EndDate_To_be_Involved']
    date_hierarchy = ('prepared_Start_DateTobeInvolved')
    list_filter = ['first_Name', 'state', ]
    list_per_page = 20
    search_fields = ['first_Name', 'state','lga']


class SpecializationAdmin(admin.ModelAdmin):
    search_fields = ['__all__']

class QualificationAdmin(admin.ModelAdmin):
    search_fields = ['__all__']

class ProfessionAdmin(admin.ModelAdmin):
    search_fields = ['__all__']

class StateAdmin(admin.ModelAdmin):
    search_fields = ['__all__']


class LgaAdmin(admin.ModelAdmin):
    search_fields = ['__all__']

class WardAdmin(admin.ModelAdmin):
    search_fields = ['__all__']


admin.site.register(Qualification, QualificationAdmin)
admin.site.register(Profession, ProfessionAdmin)
admin.site.register(State, StateAdmin)
admin.site.register(Lga, LgaAdmin)
admin.site.register(Ward, WardAdmin)
admin.site.register(Specialization, SpecializationAdmin)
# admin.site.register(Expertise, ExpertiseAdmin)
# admin.site.register(Doctor, DoctorAdmin)


