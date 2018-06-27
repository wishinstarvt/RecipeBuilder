from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.recipe_list, name='recipe_list'),
    ]