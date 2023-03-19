from django.urls import path, include
from rest_framework import routers
from .views import RecipeViewSet, TagViewSet, IngredientViewSet


app_name = 'api'

router = routers.SimpleRouter()
router.register(r'recipes', RecipeViewSet)
router.register(r'tags', TagViewSet)
router.register(r'ingredients', IngredientViewSet)

urlpatterns = [
    path('', include(router.urls))
]
