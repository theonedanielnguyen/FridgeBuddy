from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.welcome),
    path('login_page', views.login_page),
    path('registration_page', views.registration_page), 
    path('login', views.login),
    path('registration', views.registration),
    path('log_out', views.log_out),
]