import random
import string
from django.utils.text import slugify
from io import BytesIO
from rest_framework import permissions, generics, status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework import permissions, generics, status
from django.http import JsonResponse
from django.contrib.auth import login
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.http import JsonResponse
import requests
from rest_framework.authtoken.models import Token
from django.views.decorators.csrf import csrf_exempt

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from .models import User, PhoneOTP
from .serializers import (CreateUserSerialzier, 
                        UserSerializer, SerOTP)


def otp_generator():
    otp = random.randint(999, 9999)
    return otp


def send_otp(phone):

    if phone:
        
        key = otp_generator()
        phone = str(phone)
        otp_key = str(key)

        return otp_key
    else:
        return False
    
    
def post_otp(self,request):
        phone_number = self.request.data.get('phone')

        if phone_number:

            phone = str(phone_number)
            user = User.objects.filter(phone__iexact = phone)

            if user.exists():  #this means that the user already exists, no new OTP for them
                return Response({'status':False, 'detail':'User already exist. Kindly reset your password.'})

            else: #if the user doesn't exists 
                otp = send_otp(phone)
                print(phone, otp)
                if otp: #if the otp already exists, then we'll increase the PhoneOTP.count by 1, max_limit is 10
                    otp = str(otp)
                    old_otp = PhoneOTP.objects.filter(phone__iexact = phone)

                    if old_otp.exists():
                        old_otp = old_otp.first()
                        otp_count = old_otp.count

                        if otp_count > 10:
                            return Response ({
                            'status':False,
                            'detail':'You have exceeded the OTP limit. Kindly contact our customer care support.'
                            })

                        old_otp.count = otp_count + 1
                        old_otp.otp = otp
                        old_otp.save()
                        print("count increase", old_otp.count)  
                        data = PhoneOTP.objects.values().last()
                        serializer = SerOTP(data=data)
                        if serializer.is_valid():
                            return Response(serializer.data)
                        
                        return Response(serializer.errors)

                    else:
                        PhoneOTP.objects.create(
                            phone = phone,
                            otp = otp)
                        data = PhoneOTP.objects.values().last()
                        serializer = SerOTP(data=data)
                        if serializer.is_valid():
                            return Response(serializer.data)
                        
                        return Response(serializer.errors)
                        

                else:
                    return Response ({
                        'status':False,
                        'detail':'OTP sending error. Please try after sometime'
                        })


        else:
            return Response ({
                'status': False,
                'detail':'No phone number has been received. Kindly do the POST request.'
                })    