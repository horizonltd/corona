from django.contrib import admin
from . models import State, Country
# Register your models here.


class StateAdmin(admin.ModelAdmin):
    search_fields = ['__all__']

class CountryAdmin(admin.ModelAdmin):
    search_fields = ['__all__']

admin.site.register(State, StateAdmin)
admin.site.register(Country, CountryAdmin)

