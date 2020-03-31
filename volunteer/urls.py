from . import views
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import ExpertiseViewSet, DoctorViewSet

#Router
router  = routers.DefaultRouter()
router.register('doctor', DoctorViewSet)
router.register('expertise', ExpertiseViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

