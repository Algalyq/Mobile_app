from django.urls import path, include, re_path
from .views import (SendPhoneOTP, 
					ValidateOTP, 
					Register,Test )
app_name = "custom_users"

urlpatterns = [

	path('sendotp/', SendPhoneOTP.as_view()),
	path('validateotp/', ValidateOTP.as_view()),
	path('register/', Register.as_view()),
	path('test/', Test.as_view())
]
