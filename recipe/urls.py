from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.recipe_list, name='recipe_list'),
    re_path(r'^recipe/(?P<pk>\d+)/$', views.recipe_detail, name='recipe_detail'),
    ]