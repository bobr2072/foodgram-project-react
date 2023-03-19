from django.contrib import admin
from .models import Recipe, Tag, Ingredient, Cart, RecipeIngredient, Favorite


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_filter = ['author', 'name', 'tags']
    filter_horizontal = ['ingredients', 'tags']
    ordering = ('id',)
    list_display = ['name', 'author']


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ['id', 'name', 'color', 'slug']


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    ordering = ('id',)
    list_display = ('name', 'measurement_unit')
    list_filter = ('name', )


@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe',)


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe',)


@admin.register(RecipeIngredient)
class RecipeIngredientAdmin(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'amount',)
