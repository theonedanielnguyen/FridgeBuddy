from django.db import models
from datetime import datetime
from fridge.models import Fridge

class MealManager(models.Manager): 
    def add_meal_validator(self, post_data):
        errors = {}
        
        # DISH NAME VALIDATOR
        if len(post_data['dish_name']) == 0:
            errors['dish_name'] = "Please enter a dish name."

        # MEAL TIME VALIDATOR
        if not post_data['dish_time']:
            errors['dish_time'] = "Please enter a meal time."

        # DATE VALIDATOR
        dish_date = post_data['dish_date']

        if (len(post_data['dish_date'])) == 0:
            errors['dish_date'] = "Please enter a date."
            return errors

        if datetime.strptime(dish_date, '%Y-%m-%d') < datetime.today():
            errors['dish_date'] = "Sorry, the date must be set for today or later!"

        return errors

class MealPlan(models.Model):
    fridge = models.OneToOneField(Fridge, related_name="meal_plan", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)

class Meal(models.Model):
    name = models.CharField(max_length=255)
    date = models.DateTimeField()
    meal_time = models.CharField(max_length=30)
    meal_plan = models.ForeignKey(MealPlan, related_name="meals", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    last_updated = models.DateTimeField(auto_now=True)
    objects = MealManager()
