from django.shortcuts import render, redirect, render_to_response
from django.template import RequestContext
from django.contrib import messages
from .models import User
import bcrypt

def welcome(request):
    if 'user_id' in request.session:
        return redirect('/fridge/inventory')

    return render(request, 'welcome.html')

def login_page(request):
    if 'not_logged_in' in request.session:
        messages.error(request, request.session['not_logged_in'], extra_tags="login")
        del request.session['not_logged_in'] 

    if 'user_id' in request.session:
        return redirect('/fridge/inventory')

    return render(request, 'login.html')

def registration_page(request):
    if 'user_id' in request.session:
        return redirect('/fridge/inventory')

    return render(request, 'registration.html')

def registration(request):
    errors = User.objects.rego_validator(request.POST)
    if User.objects.filter(email=request.POST['email']):
        messages.error(request, 'This email already exists in the system!', extra_tags="registration")
        return redirect('/registration_page')

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags="registration")
        return redirect('/registration_page')

    else: 
        new_first_name = request.POST['first_name']
        new_last_name = request.POST['last_name']
        new_email = request.POST['email']
        new_password = request.POST['password']

        password_hash = bcrypt.hashpw(new_password.encode(), bcrypt.gensalt()).decode()

        user = User.objects.create(first_name=new_first_name, last_name=new_last_name, email=new_email, password=password_hash)

        request.session['user_id'] = user.id

        print(f'Successful! {new_first_name} {new_last_name} is now registered!')

        return redirect('/fridge/')

def login(request): 
    login_errors = User.objects.login_validator(request.POST)

    if len(login_errors) > 0:
        for key, value in login_errors.items():
            messages.error(request, value, extra_tags="login")

        return redirect('/login_page')

    else: 
        user = User.objects.filter(email=request.POST['login-email'])
        if user: 
            logged_user = user[0]

            if bcrypt.checkpw(request.POST['login-password'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id

                print(f'Successful! {logged_user.first_name} {logged_user.last_name} is logged in!')

                return redirect('/fridge/')

        
        messages.error(request, "Sorry, username and password don't match.", extra_tags="login")
        return redirect('/login_page')

def log_out(request):
    if 'user_id' in request.session:
        del request.session['user_id'] 

    return redirect('/login_page')

def handle_404(request, exception, template_name="404.html"):
    response = render_to_response(template_name)
    response.status_code = 404
    return response


