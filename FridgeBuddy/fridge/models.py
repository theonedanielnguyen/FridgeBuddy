from django.db import models
from .login_and_rego.models import User

class FridgeManager(models.Manager): 
    def create_fridge_validator(self, post_data):
        errors = {}

        # FRIDGE NAME VALIDATOR
        if len(post_data['fridge_name']) == 0:
            errors['fridge_name'] = "Please enter a fridge name."


        # PASSWORD VALIDATOR
        if len(post_data['fridge_password']) < 8:
            errors['password'] = "Password must be over 8 characters."

        if post_data['fridge_password'] != post_data['confirm_fridge_password']:
            errors['confirm_fridge_password'] = "Passwords entered do not match!"

        return errors

    def login_fridge(self, post_data):

        # FRIDGE NAME VALIDATOR
        if len(post_data['login_fridge_name']) == 0:
            errors['fridge_name'] = "Please enter a fridge name."

        return errors

class Fridge(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    members = models.ForeignKey('login_and_rego.User', related_name="fridge", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

class FridgeIngredient(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.FloatField()
    unit = models.CharField(max_length=10)
    fridge = models.ForeignKey(Fridge, related_name="contents", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

