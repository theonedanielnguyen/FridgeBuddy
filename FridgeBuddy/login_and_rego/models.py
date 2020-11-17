from django.db import models
import re
from fridge.models import Fridge
from shopping_list.models import ShoppingList

class UserManager(models.Manager):
    def rego_validator(self, post_data):
        errors = {}

        # FIRST AND LAST NAME LENGTH VALIDATOR 
        if len(post_data['first_name']) < 2:
            errors['first_name'] = "First name must be over 2 characters."

        if len(post_data['last_name']) < 2:
            errors['last_name'] = "Last name must be over 2 characters."

        NAME_REGEX = re.compile(r'^[a-zA-Z]+$')
        if not NAME_REGEX.match(post_data['first_name']):
            errors['first_name'] = "Please enter a valid first name."

        if not NAME_REGEX.match(post_data['last_name']):
            errors['last_name'] = "Please enter a valid last name."

        # EMAIL VALIDATOR
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email'] = "Please enter a valid email address."

        # PASSWORD VALIDATOR 
        if len(post_data['password']) < 8:
            errors['password'] = "Password must be over 8 characters."

        if post_data['password'] != post_data['confirm_password']:
            errors['confirm_password'] = "Passwords entered do not match!"

        return errors
    
    def login_validator(self, post_data):
        login_errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(post_data['login-email']):
            login_errors['login-email'] = "Please enter a valid email address."

        return login_errors

class User(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100)
    fridge = models.ForeignKey(Fridge, related_name="members", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()