from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=65)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    slug = models.SlugField(unique=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cover = models.ImageField(upload_to='recipes/covers/%Y/%m/%d/')

    category = models.ForeignKey(
        Category, on_delete=models.SET_NULL, null=True)
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=64)
    description = models.CharField(max_length=165)

    preparation_time = models.IntegerField()
    preparation_time_unit = models.CharField(max_length=10)

    servings = models.IntegerField()
    servings_unit = models.CharField(max_length=10)

    preparation_steps = models.CharField(max_length=5000)
    preparation_steps_is_html = models.BooleanField(default=False)

    def __str__(self):
        return self.title
