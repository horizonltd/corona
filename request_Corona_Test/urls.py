from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import RequestCoronaTestViewSet, MaterialViewSet

#Router
router  = routers.DefaultRouter()
router.register('test', RequestCoronaTestViewSet)
router.register('material', MaterialViewSet)


urlpatterns = [
    path('', include(router.urls)),
    #path('', views.AppointmentView.as_view(), name="appointment"),
]
