from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from login_and_rego.models import User
from fridge.models import Fridge
from .models import *

# Create your views here.
def meal_plan_dash(request):
    context = {
        "online_user": User.objects.get(id=request.session['user_id']),
        "meals": User.objects.get(id=request.session['user_id']).fridge.meal_plan.meals.all()
    }
    
    return render(request, 'meal_plan.html', context)

def add_meal(request):
    errors = Meal.objects.add_meal_validator(request.POST)

    if len(errors)> 0:
        for message in errors.values():
            messages.error(request, message, extra_tags="add_meal")
        return redirect('/meal_plan')

    user = User.objects.get(id=request.session['user_id'])
    new_dish = request.POST['dish_name']
    new_date = request.POST['dish_date']
    new_meal_time = request.POST['dish_time']

    new_meal = Meal.objects.create(
        name=new_dish, 
        date=new_date, 
        meal_time=new_meal_time, 
        meal_plan=user.fridge.meal_plan
    )

    return redirect('/meal_plan')

def remove_meal(request, meal_id):
    meal_to_delete = Meal.objects.get(id=meal_id)
    meal_to_delete.delete()
    return redirect('/meal_plan')