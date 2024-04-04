from django.urls import path
from .views import RecipeListView, RecipeDetailView, RecipeCreateView, RecipeImageCreateView

urlpatterns = [
    path('recipes/list', RecipeListView.as_view(), name='recipes_list'),
    path('recipe/<int:pk>', RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/add', RecipeCreateView.as_view(), name='recipe_create'),
    path('recipe/<int:pk>/add_image',
         RecipeImageCreateView.as_view(), name='recipe_add_image'),
]

app_name = 'ledger'
