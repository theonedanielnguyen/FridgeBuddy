from django.db import models
from fridge.models import Fridge

# Create your models here.
class ShoppingIngredientManager(models.Manager):
    def add_validator(self, postData):
        errors = {}

        if len(postData['ingredient']) == 0:
            errors['ingredient_name'] = "Please enter an item name."

        if len(postData['quantity']) == 0:
            errors['bad_quantity'] = "Please enter a quantity."

        return errors
    
    def remove_validator(self, postData):
        errors = {}
        if len(postData['ingredient']) == 0:
            errors['ingredient_name'] = "Please enter an item name."

        if len(postData['quantity']) == 0:
            errors['bad_quantity'] = "Please enter a quantity."

        return errors

class ShoppingList(models.Model):
    fridge = models.OneToOneField(Fridge, related_name="shopping_list", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

class ShoppingIngredient(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.FloatField()
    unit = models.CharField(max_length=10)
    shopping_list = models.ForeignKey(ShoppingList, related_name="contents", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    objects = ShoppingIngredientManager()
