from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.login_page),
    path('registration_page', views.registration_page), 
    path('login', views.login),
    path('success', views.success_rego),
    path('log_out', views.log_out)
]