# Generated by Django 2.2.4 on 2020-11-19 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meal_plan', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='meal_plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='meals', to='meal_plan.MealPlan'),
        ),
    ]
