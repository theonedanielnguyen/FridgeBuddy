from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.index),
    path('add_to_list', views.add_to_list),
    path('remove_from_list', views.remove_from_list),
    path('add_to_fridge', views.add_to_fridge),
]