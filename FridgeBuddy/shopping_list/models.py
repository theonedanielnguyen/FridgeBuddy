from django.db import models
from fridge.models import Fridge
from login_and_rego.models import User

# Create your models here.
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
