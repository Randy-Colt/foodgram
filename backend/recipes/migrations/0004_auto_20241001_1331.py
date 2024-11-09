# Generated by Django 3.2 on 2024-10-01 10:31

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_rename_description_recipe_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientrecipe',
            name='ingredients',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ingredients_recipe', to='recipes.ingredient', verbose_name='Ингридиент'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='cooking_time',
            field=models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1, 'Время приготовления не должно быть меньше 1')], verbose_name='Время приготовления'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(related_name='ingredients', through='recipes.IngredientRecipe', to='recipes.Ingredient', verbose_name='Ингридиенты'),
        ),
    ]