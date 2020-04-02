from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('hospital.urls')),
    path('api/v1/volunteer/', include('volunteer.urls')),
    path('api/v1/appointment/', include('appointment.urls')),
    path('api/v1/cases/', include('cases.urls')),
    path('api/v1/test/', include('request_Corona_Test.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
