from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from login_and_rego.models import User
from .models import Fridge, FridgeIngredient
from shopping_list.models import ShoppingList
import bcrypt

# RENDERING PAGES 
# def new_fridge_dash(request):
#     if 'user_id' not in request.session:
#         request.session['not_logged_in'] = "Please log in for access"
#         return redirect('/login_page')

#     context = {
#         "online_user": User.objects.get(id=request.session['user_id'])
#     }

#     return render(request, "no_fridge_dash.html", context)

def has_fridge_dash(request):
    if 'user_id' not in request.session:
        request.session['not_logged_in'] = "Please log in for access"
        return redirect('/')

    context = {
        "online_user": User.objects.get(id=request.session['user_id'])
    }

    return render(request, "fridge_dashboard.html", context)

def create_fridge_page(request):
    if 'user_id' not in request.session:
        request.session['not_logged_in'] = "Please log in for access"
        return redirect('/login_page')

    context = {
        "online_user": User.objects.get(id=request.session['user_id'])
    }

    return render(request, "create_fridge_page.html", context)

def join_fridge_page(request):
    if 'user_id' not in request.session:
        request.session['not_logged_in'] = "Please log in for access"
        return redirect('/login_page')

    context = {
        "online_user": User.objects.get(id=request.session['user_id'])
    }

    return render(request, "join_fridge_page.html", context)


# CREATING FRIDGE

def create_fridge_success(request):
    errors = Fridge.objects.create_fridge_validator(request.POST)

    if Fridge.objects.filter(name=request.POST['fridge_name']):
        messages.error(request, 'This fridge name already exists in the system!')
        return redirect('/fridge/new')

    if len(errors) > 0: 
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/fridge/new')

    else:

        new_fridge_name = request.POST['fridge_name']
        new_fridge_password = request.POST['fridge_password']
        new_fridge_user = User.objects.get(id=request.session['user_id'])

        password_hash = bcrypt.hashpw(new_fridge_password.encode(), bcrypt.gensalt()).decode()
        Fridge.objects.create(name=new_fridge_name, password=password_hash)
        new_fridge = Fridge.objects.last()
        ShoppingList.objects.create(fridge=new_fridge)
        new_fridge_user.fridge = new_fridge
        new_fridge_user.save()

    return redirect('/fridge/')


# JOINING FRIDGE

def join_fridge(request): 
    errors = Fridge.objects.join_fridge_validator(request.POST)

    if len(errors) > 0: 
        for key, value in errors.items():
            messages.error(request, value)

        return redirect('/fridge/join_fridge')

    else: 
        fridge_name = request.POST['existing_fridge_name']
        this_fridge = Fridge.objects.filter(name=fridge_name)
        if this_fridge: 
            logged_fridge = this_fridge[0]

            if bcrypt.checkpw(request.POST['existing_fridge_password'].encode(), logged_fridge.password.encode()):

                print(f'Successful! Logged into {fridge_name}.')

                online_user = User.objects.get(id=request.session['user_id'])
                online_user.fridge = logged_fridge
                online_user.save()

                return redirect('/fridge')

    messages.error(request, "Sorry, fridge name and password don't match.")
    return redirect('/fridge/join_fridge')


def leave_fridge(request):
    online_user = User.objects.get(id=request.session['user_id'])
    online_user.fridge = None
    online_user.save()

    return redirect('/fridge/')

# FRIDGE INVENTORY STUFF 

def display_inventory(request):
    if 'not_logged_in' in request.session:
        messages.error(request, request.session['not_logged_in'], extra_tags="login")
        del request.session['not_logged_in'] 

    this_fridge = User.objects.get(id=request.session['user_id']).fridge

    context = {
        "online_user": User.objects.get(id=request.session['user_id']),
        "fridge": User.objects.get(id=request.session['user_id']).fridge,
        "inventory": this_fridge.contents.all(),
        "members": this_fridge.members.all()
    }

    return render(request, 'inventory.html', context) 

def add_to_inventory(request):
    errors = FridgeIngredient.objects.add_ingredient_validator(request.POST)

    if len(errors) > 0: 
        for key, value in errors.items():
            messages.error(request, value)

        return redirect('/fridge/inventory')


    this_fridge = User.objects.get(id=request.session['user_id']).fridge

    new_item_name = request.POST['item_name']
    new_item_quantity = request.POST['quantity']
    new_item_unit = request.POST['unit']

    this_item = FridgeIngredient.objects.create(name=new_item_name, quantity=float(new_item_quantity), unit=new_item_unit, fridge=this_fridge)
    this_item.fridge = this_fridge

    return redirect('/fridge/inventory')

def remove_from_inventory(request, item_id):
    item_to_remove = FridgeIngredient.objects.get(id=item_id)
    item_to_remove.delete()

    return redirect('/fridge/inventory')
