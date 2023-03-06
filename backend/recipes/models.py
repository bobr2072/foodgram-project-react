from django.db import models
from users.models import User


class Ingredient(models.Model):
    class IngredientType(models.TextChoices):
        GRAMS = 'г', ('г')
        MILLILITERS = 'мл', ('мл')
        UNITS = 'шт', ('шт')

    name = models.CharField(
        blank=False,
        max_length=200,
    )
    type = models.CharField(
        choices=IngredientType.choices,
        max_length=2,
    )
    amount = models.PositiveIntegerField()


class Tag(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True,
        blank=False
    )
    color = models.CharField(
        max_length=7,
        unique=True,
        blank=False
    )
    slug = models.SlugField(
        unique=True,
        blank=False
    )


class Recipe(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        verbose_name='Автор рецепта',
        related_name='recipes'
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        verbose_name='Ингредиенты',
        related_name='recipes'
    )
    tags = models.ManyToManyField(
        Tag,
        verbose_name='Теги',
        related_name='recipes'
    )
    image = models.ImageField(
        upload_to='recipes/',
        verbose_name='Изображение',
        blank=False
    )
    name = models.CharField(
        max_length=30,
        verbose_name='Название рецепта',
        blank=False
    )
    text = models.TextField(
        verbose_name='Описание',
        blank=False
    )
    cooking_time = models.PositiveIntegerField(
        verbose_name='Время приготовления',
        blank=False
    )


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(
        Ingredient,
        on_delete=models.CASCADE
    )
    ingridient = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    amount = models.IntegerField(null=False)


class RecipeTag(models.Model):
    recipe = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE
    )
    tag = models.ForeignKey(
        Recipe,
        on_delete=models.CASCADE
    )
