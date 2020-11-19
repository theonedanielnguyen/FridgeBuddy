from django.urls import path, include 
from . import views

urlpatterns = [
    path('', views.has_fridge_dash), 
    path('new', views.create_fridge_page),
    path('new_fridge_success', views.create_fridge_success),
    path('join_fridge', views.join_fridge_page),
    path('join_success', views.join_fridge),
    path('leave', views.leave_fridge),
    path('inventory', views.display_inventory),
    path('inventory/add_item', views.add_to_inventory),
    path('inventory/remove_item', views.remove_from_inventory)
]