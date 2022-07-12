from django.contrib import admin

from .models import Category, Recipe


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )


class RecipeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Recipe, RecipeAdmin)
