from django.db.models import Q
from django.http import Http404
from django.shortcuts import get_list_or_404, get_object_or_404, render
from utils.pagination import pagination

from .models import Recipe


# Create your views here.
def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')

    page_object, pagination_range = pagination(
        request, queryset=recipes, per_page=9)

    return render(request, 'pages/home.html', context={
        'recipes': page_object,
        'pagination_range': pagination_range,
    })


def category(request, id):
    recipes = get_list_or_404(
        Recipe.objects.filter(
            is_published=True,
            category__id=id
        ).order_by('-id')
    )

    page_object, pagination_range = pagination(
        request, queryset=recipes, per_page=9)

    return render(request, 'pages/category.html', context={
        'recipes': page_object,
        'pagination_range': pagination_range,
        'title': f'{recipes[0].category.name}'
    })


def recipe(request, id):
    recipe = get_object_or_404(Recipe, id=id, is_published=True)

    return render(request, 'pages/recipe.html', context={
        'recipe': recipe,
        'is_detail_page': True,
    })


def search(request):
    search_term = request.GET.get('q', '').strip()
    if not search_term:
        raise Http404()

    recipes = Recipe.objects.filter(
        # Need postgres to use title__search
        Q(
            Q(title__icontains=search_term) |
            Q(description__icontains=search_term),
        ),
        is_published=True,
    ).order_by('-id')

    page_object, pagination_range = pagination(
        request, queryset=recipes, per_page=9)

    return render(request, 'pages/search.html', context={
        'page_title': f'Search for "{search_term}"',
        'search_term': search_term,
        'recipes': page_object,
        'pagination_range': pagination_range,
        'additional_url_query': f'&q={search_term}',
    })
