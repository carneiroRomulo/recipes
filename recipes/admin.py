from django.contrib import admin
from .models import Category, Recipe

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
admin.site.register(Category, CategoryAdmin)

class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
admin.site.register(Recipe, RecipeAdmin)