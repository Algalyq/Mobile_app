from rest_framework import serializers
from .models import Uniforms, SeasonTicket


class SeasonSerializer(serializers.ModelSerializer):
    class Meta:
        model = SeasonTicket
        fields = ('__all__')
        
class UniformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Uniforms
        fields = ('__all__')
        