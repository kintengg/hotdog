from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView

from .models import Recipe, RecipeImage
from .forms import RecipeForm, RecipeImageForm


class RecipeListView(ListView):
    model = Recipe
    template_name = 'recipes_list.html'


class RecipeDetailView(LoginRequiredMixin, DetailView):
    model = Recipe
    template_name = 'recipe.html'


class RecipeCreateView(LoginRequiredMixin, CreateView):
    model = Recipe
    template_name = "recipe_create.html"
    form_class = RecipeForm


class RecipeImageCreateView(LoginRequiredMixin, CreateView):
    model = RecipeImage
    template_name = "recipe_add_image.html"
    form_class = RecipeImageForm

    def get_success_url(self):
        return reverse_lazy("ledger:recipe_detail", kwargs={"pk": self.object.recipe.pk})

    def form_valid(self, form):
        form.instance.recipe = Recipe.objects.get(pk=self.kwargs["pk"])
        return super().form_valid(form)
