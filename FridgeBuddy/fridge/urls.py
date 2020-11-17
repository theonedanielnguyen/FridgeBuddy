from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.has_fridge_dash)
]