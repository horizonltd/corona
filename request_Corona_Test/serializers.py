from rest_framework import serializers
from .import models 

class RequestCoronaTestSerializer(serializers.ModelSerializer):
    #state = StateSerializer(many=True)
    #presenter = PresenterSerializer(many=False)

    class Meta:
        model = models.RequestCoronaTest
        fields = ('__all__')
        #This help to view the level of hidden relationship
        depth=1

class MaterialSerializer(serializers.ModelSerializer):
    #state = StateSerializer(many=True)
    #presenter = PresenterSerializer(many=False)

    class Meta:
        model = models.Material
        fields = ('__all__')
        #This help to view the level of hidden relationship
        depth=1


