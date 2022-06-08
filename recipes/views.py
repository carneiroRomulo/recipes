from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Recipe


# Create your views here.
def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    return render(request, 'pages/home.html', context={
        'recipes': recipes,
    })


def category(request, id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            is_published=True,
            category__id=id
        ).order_by('-id')
    )

    return render(request, 'pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name}'
    })


def recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id, is_published=True)

    return render(request, 'pages/recipe.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })
