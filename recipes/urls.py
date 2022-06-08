from django.urls import include, path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('recipe/<int:id>/', views.recipe, name="recipe"),
]