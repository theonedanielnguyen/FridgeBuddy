from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.meal_plan_dash), 
    path('add_meal', views.add_meal),
    path('remove_meal/<int:meal_id>', views.remove_meal)
]