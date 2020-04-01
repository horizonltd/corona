from rest_framework import serializers
from .import models


class VolunteerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Volunteer
        fields = [
            'entryID',
            'first_Name',
            'middle_Name',
            'surname',
            'highest_Qualification',
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
        ]
        #This help to view the level of hidden relationship
        depth=1

# class DoctorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = models.Doctor
#         fields = [
#             'name',
#             'speciality',
#             'picture',
#             'details',
#             'experience',
#             'expertise',
#             'twitter',
#             'facebook',
#             'instagram',
#         ]
#         #This help to view the level of hidden relationship
#         depth=1
# class ExpertiseSerializer(serializers.ModelSerializer):
#     doctors = DoctorSerializer(many=True)

#     class Meta:
#         model = models.Expertise
#         fields = [
#             'name',
#             'doctors',
#         ]
#         #This help to view the level of hidden relationship
#         depth=1











