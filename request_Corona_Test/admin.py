from django.contrib import admin
from .models import RequestCoronaTest, Material, State, Lga, Ward


class StateAdmin(admin.ModelAdmin):
    search_fields = ['__all__']


class LgaAdmin(admin.ModelAdmin):
    search_fields = ['__all__']

class WardAdmin(admin.ModelAdmin):
    search_fields = ['__all__']

admin.site.register(State, StateAdmin)
admin.site.register(Lga, LgaAdmin)
admin.site.register(Ward, WardAdmin)


@admin.register(RequestCoronaTest)
class RequestCoronaTestAdmin(admin.ModelAdmin):
    list_display = ['name', 'phone', 'email', 'date', 'preparedDateOfTest']
    date_hierarchy = ('preparedDateOfTest')
    list_filter = ['name', 'phone', ]
    list_per_page = 20
    search_fields = ['name', 'preparedDateOfTest', ]

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'author', 'material', 'date']
    date_hierarchy = ('date')
    list_filter = ['date', 'title', ]
    list_per_page = 20
    search_fields = ['title', 'description', ]
