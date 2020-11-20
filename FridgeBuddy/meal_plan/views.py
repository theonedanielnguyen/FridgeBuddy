from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from login_and_rego.models import User
from fridge.models import Fridge
from .models import *

# Create your views here.
def meal_plan_dash(request):
    if 'user_id' not in request.session:
        request.session['not_logged_in'] = "Please log in for access"
        return redirect('/login_page')

    context = {
        "online_user": User.objects.get(id=request.session['user_id']),
        "fridge": User.objects.get(id=request.session['user_id']).fridge,
        "meals": User.objects.get(id=request.session['user_id']).fridge.meal_plan.meals.all().order_by('date')
    }
    
    return render(request, 'meal_plan.html', context)

def add_meal(request):
    if 'user_id' not in request.session:
        request.session['not_logged_in'] = "Please log in for access"
        return redirect('/login_page')

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
    if 'user_id' not in request.session:
        request.session['not_logged_in'] = "Please log in for access"
        return redirect('/login_page')

    meal_to_delete = Meal.objects.get(id=meal_id)
    meal_to_delete.delete()
    return redirect('/meal_plan')