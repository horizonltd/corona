from django.urls import path
from . import views

urlpatterns = [
    path('', views.AppointmentView.as_view(), name="appointment"),
]







# from . import views
# from django.urls import path
# from django.conf.urls import include
# from rest_framework import routers
# from .views import TestCenterViewSet, AppointmentViewSet

# #Router
# router  = routers.DefaultRouter()
# router.register('test', TestCenterViewSet)
# router.register('appointment', AppointmentViewSet)


# urlpatterns = [
#     path('', include(router.urls)),
#     #path('', views.AppointmentView.as_view(), name="appointment"),
# ]
