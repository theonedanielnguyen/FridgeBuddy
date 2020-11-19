from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.meal_plan_dash)
]