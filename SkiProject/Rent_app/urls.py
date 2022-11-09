
from django.contrib import admin
from django.urls import path, include
from .views import UniformsView, SeasonView
urlpatterns = [
    path('uniform/', UniformsView.as_view()),
    path('season/', SeasonView.as_view())
]