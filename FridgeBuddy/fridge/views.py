from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from login_and_rego.models import User
from .models import Fridge, FridgeIngredient
import bcrypt

# CREATE/JOIN FRIDGE STUFF
def new_fridge_dash(request):
    if 'user_id' not in request.session:
        request.session['not_logged_in'] = "Please log in for access"
        return redirect('/login_page')

    context = {
        "online_user": User.objects.get(id=request.session['user_id'])
    }

    return render(request, "no_fridge_dash.html", context)

def create_fridge_page(request):
    if 'user_id' not in request.session:
        request.session['not_logged_in'] = "Please log in for access"
        return redirect('/login_page')

    context = {
        "online_user": User.objects.get(id=request.session['user_id'])
    }

    return render(request, "create_fridge_page.html", context)

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
        new_fridge = Fridge.objects.create(name=new_fridge_name, password=password_hash, members=new_fridge_user)

    return redirect('/fridge')

def has_fridge_dash(request):
    if 'user_id' not in request.session:
        request.session['not_logged_in'] = "Please log in for access"
        return redirect('/')

    context = {
        "online_user": User.objects.get(id=request.session['user_id'])
    }

    return render(request, "fridge_dashboard.html", context)

def join_fridge_page(request):
    if 'user_id' not in request.session:
        request.session['not_logged_in'] = "Please log in for access"
        return redirect('/login_page')

    context = {
        "online_user": User.objects.get(id=request.session['user_id'])
    }

    return render(request, "join_fridge.html", context)

def join_fridge(request): 
    fridge_name = request.POST['existing_fridge_name']
    fridge_password = request.post['existing_fridge_password']

    join_fridge_errors = Fridge.objects.join_fridge_validator(request.POST)

    if len(join_fridge_errors) > 0: 
        for key, value in join_fridge_errors.items():
            messages.error(request, value)

        return redirect('/fridge/join_fridge')

    else: 
        this_fridge = Fridge.objects.filter(name=fridge_name)
        if this_fridge: 
            logged_fridge = this_fridge[0]

            if bcrypt.checkpw(fridge_password.encode(), logged_fridge.password.encode()):

                print(f'Successful! {logged_user.first_name} {logged_user.last_name} is logged in!')

                online_user = User.objects.get(id=request.session['user_id'])
                online_user.fridge = this_fridge
                online_user.save()

                return redirect('/fridge')

    messages.error(request, "Sorry, fridge name and password don't match.")
    return redirect('/fridge/join_fridge')

# FRIDGE INVENTORY STUFF 

def display_inventory(request):
    context = {
        "inventory": FridgeIngredient.objects.all()
    }

    return render(request, 'inventory.html', context) 

def add_to_inventory(request):
    this_fridge = Fridge.objects.get(id=request.session['fridge_id'])

    new_item_name = request.POST['item_name']
    new_item_quantity = request.POST['quantity']
    new_item_unit = request.POST['unit']

    this_item = FridgeIngredient.objects.create(name=new_item_name, quantity=float(new_item_quantity), unit=new_item_unit, fridge=this_fridge)

    return redirect(f'/fridge/inventory')

def remove_from_inventory(request, item_id):
    item_to_remove = FridgeIngredient.objects.get(id=item_id)
    item_to_remove.delete()

    return redirect(f'/fridge/inventory')