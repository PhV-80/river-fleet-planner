from rest_framework import serializers
from .models import Ship, Voyage

class ShipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ship
        fields= [
            'id',
            'name',
            'capacity',
            'status',
            'created_at',
            'updated_at'
        ]
        read_only_fields = ['id','created_at','updated_at']

class VoyageSerializer(serializers.ModelSerializer):
    ship_details = ShipSerializer(source='ship', read_only=True)

    class Meta:
        model = Voyage
        fields = '__all__'
        read_only_fields = ['id','created_at','updated_at']

    def validate(self, attrs):
        instance = Voyage(**attrs)
        instance.clean()
        return attrs