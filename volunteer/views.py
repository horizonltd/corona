from .models import Volunteer, ReportCase
from .serializers import VolunteerSerializer, ReportCaseSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import TokenAuthentication
# Create your views here.
#psycopg2-2.8.4-cp27-cp27m-win32.whl

# class DoctorViewSet(viewsets.ModelViewSet):
#     queryset = Doctor.objects.all()
#     serializer_class = DoctorSerializer
#     authentication_classes = (TokenAuthentication, )
#     permission_classes = (AllowAny, )

# class ExpertiseViewSet(viewsets.ModelViewSet):
#     queryset = Expertise.objects.all()
#     serializer_class = ExpertiseSerializer
#     authentication_classes = (TokenAuthentication, )
#     permission_classes = (AllowAny, )


class VolunteerViewSet(viewsets.ModelViewSet):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )

class ReportCaseViewSet(viewsets.ModelViewSet):
    queryset = ReportCase.objects.all()
    serializer_class = ReportCaseSerializer
    authentication_classes = (TokenAuthentication, )
    permission_classes = (AllowAny, )


# class StateViewSet(viewsets.ModelViewSet):
#     queryset = State.objects.all()
#     serializer_class = StateSerializer
#     authentication_classes = (TokenAuthentication, )
#     permission_classes = (AllowAny, )

# class LgaViewSet(viewsets.ModelViewSet):
#     queryset = Lga.objects.all()
#     serializer_class = LgaSerializer
#     authentication_classes = (TokenAuthentication, )
#     permission_classes = (AllowAny, )

# class WardViewSet(viewsets.ModelViewSet):
#     queryset = Ward.objects.all()
#     serializer_class = WardSerializer
#     authentication_classes = (TokenAuthentication, )
#     permission_classes = (AllowAny, )

# class QualificationViewSet(viewsets.ModelViewSet):
#     queryset = Qualification.objects.all()
#     serializer_class = QualificationSerializer
#     authentication_classes = (TokenAuthentication, )
#     permission_classes = (AllowAny, )

# class SpecializationViewSet(viewsets.ModelViewSet):
#     queryset = Specialization.objects.all()
#     serializer_class = SpecializationSerializer
#     authentication_classes = (TokenAuthentication, )
#     permission_classes = (AllowAny, )

# class ProfessionViewSet(viewsets.ModelViewSet):
#     queryset = Profession.objects.all()
#     serializer_class = ProfessionSerializer
#     authentication_classes = (TokenAuthentication, )
#     permission_classes = (AllowAny, )





