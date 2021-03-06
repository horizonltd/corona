from django.contrib import admin
from . models import State, Country, TestCenter
# Register your models here.




class TestCenterAdmin(admin.ModelAdmin):
    search_fields = ['__all__']

admin.site.register(TestCenter, TestCenterAdmin)



class StateAdmin(admin.ModelAdmin):
    search_fields = ['__all__']

class CountryAdmin(admin.ModelAdmin):
    search_fields = ['__all__']

admin.site.register(State, StateAdmin)
admin.site.register(Country, CountryAdmin)

