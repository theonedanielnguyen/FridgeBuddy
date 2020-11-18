from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from login_and_rego.models import User
from .models import *
from fridge.models import Fridge

# Create your views here.
def index(request):
    context = {
    #     "user" : User.objects.get(id=request.session['user_id'])
    #     "shopping_list" : User.objects.get(id=request.session['user_id']).shopping_list.contents.all()
    }
    return render(request, "shopping.html", context)

def add_to_list(request):
    errors = ShoppingIngredient.objects.add_validator(request.POST)
    if len(errors)> 0:
        for message in errors.values():
            messages.error(request, message)
        return redirect('/shopping_list')
    # user = User.objects.get(id=request.session['user_id'])
    ShoppingIngredient.objects.create(
        name = request.POST['ingredient'],
        quantity = request.POST['quantity'],
        unit = request.POST['unit'],
        # shopping_list = user.fridge.shopping_list,
    )
    return redirect('/shopping_list')

def remove_from_list(request):
    # user = User.objects.get(id=request.session['user_id'])
    
    return redirect('/shopping_list')