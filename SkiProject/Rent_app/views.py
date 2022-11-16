from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Ski_directory, Resort_directory
from .serializers import SkiSerializer, BootsSerializer,SubscSerializer,ResortSerializer
import requests
from rest_framework.response import Response
from .models import Boot_directory, Ski_directory, Subsc_directory, Resort_directory
class SkiView(APIView):
    def get(self,request):
        ski = Ski_directory.objects.all()
        serializer = SkiSerializer(ski, many=True)
        return Response(serializer.data)


class ResortView(APIView):

    def get(self,request):
        resort = Resort_directory.objects.all()
        serializer = ResortSerializer(resort,many=True)
        return Response(serializer.data)