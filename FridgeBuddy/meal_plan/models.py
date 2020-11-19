from django.db import models
from fridge.models import Fridge

class MealPlan(models.Model):
    fridge = models.OneToOneField(Fridge, related_name="meal_plan", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

class Meal(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    meal_time = models.CharField(max_length=30)
    meal_plan = models.OneToOneField(MealPlan, related_name="meal", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
