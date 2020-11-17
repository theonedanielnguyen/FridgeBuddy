from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from login_and_rego.models import User
from .models import Fridge
import bcrypt

# Create your views here.
def new_fridge_dash(request):
    if 'user_id' not in request.session:
        request.session['not_logged_in'] = "Please log in for access"
        return redirect('/login_page')

    context = {
        "online_user": User.objects.get(id=request.session['user_id'])
    }

    return render(request, "no_fridge_dash.html", context)

def create_fridge_page(request):
    context = {
        "online_user": User.objects.get(id=request.session['user_id'])
    }

    return render(request, "create_fridge_page.html", context)

def create_fridge_success(request):
    errors = Fridge.objects.create_fridge_validator(request.POST)

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

    return render(request, "fridge_dash.html", context)

    
