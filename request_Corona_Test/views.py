from .models import RequestCoronaTest, Material
from .serializers import RequestCoronaTestSerializer, MaterialSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
# Create your views here.
#psycopg2-2.8.4-cp27-cp27m-win32.whl



class RequestCoronaTestViewSet(viewsets.ModelViewSet):
    queryset = RequestCoronaTest.objects.all()
    serializer_class = RequestCoronaTestSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )