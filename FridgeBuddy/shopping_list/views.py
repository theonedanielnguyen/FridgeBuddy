from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from login_and_rego.models import User
from .models import *
from fridge.models import Fridge

# Create your views here.
def index(request):
    context = {
        "user" : User.objects.get(id=request.session['user_id']),
        "shopping_list" : User.objects.get(id=request.session['user_id']).fridge.shopping_list.contents.all()
    }
    return render(request, "shopping.html", context)

def add_to_list(request):
    errors = ShoppingIngredient.objects.add_validator(request.POST)

    if len(errors)> 0:
        for message in errors.values():
            messages.error(request, message, extra_tags="add")
        return redirect('/shopping_list')

    user = User.objects.get(id=request.session['user_id'])
    if user.fridge.shopping_list.contents.filter(name=request.POST['ingredient']).exists():
        if request.POST['unit'] != user.fridge.shopping_list.contents.get(name=request.POST['ingredient']).unit:
            messages.error(request, "Units must match the unit of the target item", extra_tags="add")
            return redirect('/fridge/inventory')
        new_value = user.fridge.shopping_list.contents.get(name=request.POST['ingredient']).quantity
        new_value += float(request.POST['quantity'])
        ingredient = user.fridge.shopping_list.contents.get(name=request.POST['ingredient'])
        ingredient.quantity = new_value
        ingredient.save()

    else:
        ShoppingIngredient.objects.create(
            name = request.POST['ingredient'],
            quantity = float(request.POST['quantity']),
            unit = request.POST['unit'],
            shopping_list = user.fridge.shopping_list,
        )
        
    return redirect('/shopping_list')

def remove_from_list(request):
    errors = ShoppingIngredient.objects.remove_validator(request.POST)

    if len(errors)> 0:
        for message in errors.values():
            messages.error(request, message, extra_tags="remove")
        return redirect('/shopping_list')

    user = User.objects.get(id=request.session['user_id'])
    if user.fridge.shopping_list.contents.filter(name=request.POST['ingredient']).exists() == False:
        print("error1")
        messages.error(request, "Item does not exist in shopping list", extra_tags="remove")
        return redirect('/shopping_list')

    if float(request.POST['quantity']) > user.fridge.shopping_list.contents.get(name=request.POST['ingredient']).quantity:
        print("error2")
        messages.error(request,"Quantity removed may not be greater than quantity possessed", extra_tags="remove")
        return redirect('/shopping_list')

    if request.POST['unit'] != user.fridge.shopping_list.contents.get(name=request.POST['ingredient']).unit:
        print("error3") 
        messages.error(request, "Units must match the unit of the target item", extra_tags="remove")
        return redirect('/shopping_list')

    new_value = user.fridge.shopping_list.contents.get(name=request.POST['ingredient']).quantity
    new_value -= float(request.POST['quantity'])
    ingredient = user.fridge.shopping_list.contents.get(name=request.POST['ingredient'])
    ingredient.quantity = new_value
    ingredient.save()

    if ingredient.quantity == 0:
        ingredient.delete()

    return redirect('/shopping_list')