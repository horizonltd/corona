from rest_framework import serializers
from .import models

class TestCenterSerializer(serializers.ModelSerializer):
    #state = StateSerializer(many=True)
    #presenter = PresenterSerializer(many=False)

    class Meta:
        model = models.TestCenter
        fields = [
            'name',
            'address',
            'picture',
            'latitude',
            'longitude',
            'details',
            ]
        #This help to view the level of hidden relationship
        depth=1

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.State
        fields = [
            'country',
            'state',
            'date',
            'confirmed',
            'death',
            'recovered',
        ]
        #This help to view the level of hidden relationship
        depth=1

class CountrySerializer(serializers.ModelSerializer):
    state = StateSerializer(many=True)
    #presenter = PresenterSerializer(many=False)

    class Meta:
        model = models.Country
        fields = [
            'country',
            'date',
            'confirmed',
            'death',
            'recovered',
            'state',
            ]
        #This help to view the level of hidden relationship
        depth=1



# class State(models.Model):
#     country = models.OneToOneField(Country, on_delete=models.CASCADE, related_name='state')
#     state = models.CharField(max_length=100, default='')
#     date = models.DateField(default=2019-12-13)
#     confirmed = models.CharField(max_length=100, default='')
#     death = models.CharField(max_length=100, default='')
#     recovered = models.CharField(max_length=100, default='')

#     def __str__(self):
#         return self.state






