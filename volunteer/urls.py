from . import views
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import ExpertiseViewSet, DoctorViewSet, VolunteerViewSet

#Router
router  = routers.DefaultRouter()
router.register('doctor', DoctorViewSet)
router.register('expertise', ExpertiseViewSet)
router.register('volunteer', VolunteerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

