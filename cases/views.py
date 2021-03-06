from .models import State, Country, TestCenter
from .serializers import StateSerializer, CountrySerializer,TestCenterSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
# Create your views here.
#psycopg2-2.8.4-cp27-cp27m-win32.whl



class TestCenterViewSet(viewsets.ModelViewSet):
    queryset = TestCenter.objects.all()
    serializer_class = TestCenterSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )

class StateViewSet(viewsets.ModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )

class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )





