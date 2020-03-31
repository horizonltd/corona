from django.urls import path
from . import views
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import StateViewSet, CountryViewSet

#Router
router  = routers.DefaultRouter()
router.register('state', StateViewSet)
router.register('country', CountryViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

