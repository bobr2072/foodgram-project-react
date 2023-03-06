from rest_framework import serializers
from recipes.models import Recipe, Tag, Ingredient
from users.models import User
from djoser.serializers import UserCreateSerializer, UserSerializer


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['id', 'name', 'color', 'slug']


class IngredientSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'amount', 'type']


class RecipeSerializer(serializers.ModelSerializer):
    ingredients = IngredientSerializer(many=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = Recipe
        fields = [
            'id', 'author', 'name', 'image', 'text', 'ingredients', 'tags',
            'cooking_time'
        ]


class DefaultUserCreateSerializer(UserCreateSerializer):

    class Meta:
        model = User
        fields = '__all__'


class DefaultUserSerializer(UserSerializer):

    class Meta:
        model = User
        fields = '__all__'
