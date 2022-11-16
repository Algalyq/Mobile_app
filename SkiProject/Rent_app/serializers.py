from rest_framework import serializers
from .models import Boot_directory, Ski_directory, Subsc_directory, Resort_directory


class BootsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boot_directory
        fields = ('__all__')


class SkiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ski_directory
        fields = ('__all__')

class SubscSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Subsc_directory
        fields = ('__all__')

class ResortSerializer(serializers.ModelSerializer):
    ski = SkiSerializer(many=True)
    subsc = SubscSerializer(many=True)
    boot = BootsSerializer(many=True) 
    class Meta:
        model = Resort_directory
        fields = ['resort_name','resort_address','ski','subsc','boot']

        