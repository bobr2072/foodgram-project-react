from django.contrib import admin
from django.contrib.admin import display

from .models import Cart, Favorite, Ingredient, Recipe, RecipeIngredient, Tag


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_filter = ['author', 'name', 'tags']
    filter_horizontal = ('ingredients', 'tags')
    readonly_fields = ('added_in_favorites',)
    ordering = ('id',)
    list_display = ('name', 'author', 'added_in_favorites')

    @display(description='Количество в избранных')
    def added_in_favorites(self, obj):
        return obj.favorites.count()


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
