from django.shortcuts import render

from utils.fake_data import make_recipe

# Create your views here.
def home(request):
    return render(request, 'pages/home.html', context={
        'recipes': [make_recipe() for _ in range(10)],
    })

def recipe(request, id):
    return render(request, 'pages/recipe.html', context={
        'recipe': make_recipe(),
        'is_detail_page': True,
    })