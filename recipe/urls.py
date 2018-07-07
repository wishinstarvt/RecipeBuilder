from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.recipe_list, name='recipe_list'),
    path('recipe/(<pk>\d+)/', views.recipe_detail, name='recipe_detail'),
    path('recipe/new/', views.recipe_new, name='recipe_new'),
    path('recipe/(<pk>\d+)/edit/', views.recipe_edit, name='recipe_edit'),
    path('recipe/(<pk>\d+)/remove/', views.recipe_remove, name='recipe_remove'),
    ]