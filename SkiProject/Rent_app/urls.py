
from django.contrib import admin
from django.urls import path, include
from .views import SkiView, ResortView
urlpatterns = [
    path('ski/', SkiView.as_view()),
    path('resort/',ResortView.as_view())
]