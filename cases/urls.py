from django.urls import path
from . import views
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import StateViewSet, CountryViewSet, TestCenterViewSet

#Router
router  = routers.DefaultRouter()
router.register('state', StateViewSet)
router.register('country', CountryViewSet)
router.register('center', TestCenterViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

