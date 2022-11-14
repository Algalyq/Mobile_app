from django.urls import path, include, re_path
from .views import (Test, LoginAPIView, UserAPIView)
app_name = "custom_users"

urlpatterns = [

	# path('register/', Register.as_view()),
	path('test/', Test.as_view()),
	path('login', LoginAPIView.as_view()),
	path('user/', UserAPIView.as_view())
]
