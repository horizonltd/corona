from rest_framework import serializers
from .import models


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.State
        fields = [
            'name',
            ]
        #This help to view the level of hidden relationship

class LgaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.State
        fields = [
            'name',
        ]
        #This help to view the level of hidden relationship


class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Ward
        fields = [
            'name',
        ]
        #This help to view the level of hidden relationship


class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Specialization
        fields = [
            'name',
        ]
        #This help to view the level of hidden relationship

class ProfessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Profession
        fields = [
            'name',
        ]
        #This help to view the level of hidden relationship



class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Qualification
        fields = [
            'name',
        ]
        #This help to view the level of hidden relationship

class VolunteerSerializer(serializers.ModelSerializer):
    # state = StateSerializer()
    # lga = LgaSerializer()
    # ward = WardSerializer()
    # specialization = SpecializationSerializer()
    # qualification = QualificationSerializer()
    # profession = ProfessionSerializer()

    class Meta:
        model = models.Volunteer
        fields = [
            'entryID',
            'first_Name',
            'middle_Name',
            'surname',
            'dob',
            'sex',
            'state',
            'lga',
            'ward',
            'polling_Unit',
            'geolocation',
            'prepared_State_of_To_Be_Involved',
            'prepared_Start_DateTobeInvolved',
            'prepared_EndDate_To_be_Involved',
            'prepared_Days_To_be_Involved',
            'email',
            'phone_Number',
            'date_Of_Entry',
            'picture',
            'qualification',
            'specialization',
            'profession',
        ]
        #This help to view the level of hidden relationship
        depth=1



























class ReportCaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ReportCase
        fields = [
            'first_Name',
            'middle_Name',
            'surname',
            'sex',
            'state',
            'lga',
            'ward',
            'polling_Unit',
            'geolocation',
            'email',
            'phone_Number',
            'description',
            'reportDate',
        ]
        #This help to view the level of hidden relationship
        depth=1








