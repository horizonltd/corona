from rest_framework import serializers
from .import models

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Doctor
        fields = [
            'name',
            'speciality',
            'picture',
            'details',
            'experience',
            'expertise',
            'twitter',
            'facebook',
            'instagram',
        ]
        #This help to view the level of hidden relationship
        depth=1
class ExpertiseSerializer(serializers.ModelSerializer):
    doctors = DoctorSerializer(many=True)

    class Meta:
        model = models.Expertise
        fields = [
            'name',
            'doctors',
        ]
        #This help to view the level of hidden relationship
        depth=1











