from django.db import models

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

    def join_fridge_validator(self, post_data):
        errors = {}

        # FRIDGE NAME VALIDATOR
        if len(post_data['existing_fridge_name']) == 0:
            errors['existing_fridge_name'] = "Please enter a fridge name."

        return errors

class FridgeIngredientManager(models.Manager):
    def add_ingredient_validator(self, post_data):
        errors = {}

        # FRIDGE INGREDIENT NAME VALIDATOR
        if len(post_data['item_name']) == 0:
            errors['item_name'] = "Please enter an item name."

        if len(post_data['quantity']) == 0:
            errors['quantity'] = "Please enter a quantity."

        return errors

    def remove_ingredient_validator(self, post_data):
        errors = {}

        if len(post_data['item_name']) == 0:
            errors['item_name'] = "Please enter an item name."

        if len(post_data['quantity']) == 0:
            errors['quantity'] = "Please enter a quantity."

        return errors

class Fridge(models.Model):
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    objects = FridgeManager()

class FridgeIngredient(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.FloatField()
    unit = models.CharField(max_length=10)
    fridge = models.ForeignKey(Fridge, related_name="contents", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    objects = FridgeIngredientManager()

