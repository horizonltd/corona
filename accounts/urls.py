from rest_framework import routers
from accounts.views import UserViewSet
from django.urls import path, include
from rest_framework_jwt.views import refresh_jwt_token, obtain_jwt_token

router = routers.DefaultRouter()
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    #path('auth/', include('rest_auth.urls')),
    path('api/login/', obtain_jwt_token),
    path('api/login/refresh', refresh_jwt_token),

]