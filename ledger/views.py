from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Recipe


def recipes_list(request):
    recipes = Recipe.objects.all()
    ctx = { "recipes": recipes }
    return render(request, 'recipes_list.html', ctx)


def recipe_details(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    ctx = { "recipe": recipe }
    return render(request, 'recipe.html', ctx)


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes_list.html'


class RecipeDetailView(DetailView):
    model = Recipe
    template_name = 'recipe.html'