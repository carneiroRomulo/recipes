from django.urls import path

from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name='home'),

    path('recipe/search/', views.search, name='search'),
    path('recipe/category/<int:id>/', views.category, name='category'),
    path('recipe/<int:id>/', views.recipe, name='recipe'),
]
