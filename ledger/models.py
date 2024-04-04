from django.db import models
from django.urls import reverse

from datetime import datetime

from accounts import models as profile_models


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('ledger:recipes-list', args=[self.pk])


class Recipe(models.Model):
    name = models.CharField(max_length=100)
    author = models.ForeignKey(
        profile_models.Profile,
        db_column="user",
        null=True,
        on_delete=models.CASCADE,
        related_name="profile"
    )
    created_on = models.DateTimeField(default=datetime.now, blank=True)
    updated_on = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}' .format(self.name)

    def get_absolute_url(self):
        return reverse('ledger:recipe-details', args=[self.pk])
    
    class Meta:
        ordering = ['name']


class RecipeIngredient(models.Model):
    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(
        'Ingredient',
        on_delete=models.CASCADE,
        related_name="recipe"
        )
    recipe = models.ForeignKey(
        'Recipe',
        on_delete=models.CASCADE,
        related_name="ingredients"
        )