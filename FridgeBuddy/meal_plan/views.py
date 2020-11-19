from django.shortcuts import render, HttpResponse, redirect
from login_and_rego.models import User
from fridge.models import Fridge

# Create your views here.
def meal_plan_dash(request):
    context = {
        "online_user": User.objects.get(id=request.session['user_id'])
    }
    
    return render(request, 'meal_plan.html', context)