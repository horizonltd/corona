from .models import Expertise, Doctor
from .serializers import ExpertiseSerializer, DoctorSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
# Create your views here.
#psycopg2-2.8.4-cp27-cp27m-win32.whl

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )

class ExpertiseViewSet(viewsets.ModelViewSet):
    queryset = Expertise.objects.all()
    serializer_class = ExpertiseSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )





