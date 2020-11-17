from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.has_fridge_dash), 
    path('/new_user', views.new_fridge_dash),
    path('/new', views.create_fridge_page),
    path('/new_fridge_success', views.create_fridge_success),
    path('/join_fridge', views.join_fridge_page),
    path('/join_success', views.join_fridge)
]