from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Uniforms,SeasonTicket
from .serializers import UniformSerializer,SeasonSerializer
class UniformsView(APIView):
    
    def get(self,request):
        unifoms = Uniforms.objects.all()
        serializer = UniformSerializer(unifoms,many=True)
        return Response(serializer.data)

class SeasonView(APIView):
    
    def get(self,request):
        season = SeasonTicket.objects.all()
        serializer = SeasonSerializer(season, many=True)
        return Response(serializer.data)