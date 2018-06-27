from django.shortcuts import render

def recipe_list(request):
    return render(request, 'recipe/recipe_list.html', {})
