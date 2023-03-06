from django.urls import path, include
from rest_framework import routers
from .views import RecipeViewSet, TagViewSet, IngredientViewSet
#from users.views import UserViewSet


app_name = 'api'

router = routers.SimpleRouter()
router.register(r'recipes', RecipeViewSet)
#router.register(r'users', UserViewSet)
router.register(r'tags', TagViewSet)
router.register(r'ingredients', IngredientViewSet)

urlpatterns = [
    path('auth/', include('djoser.urls.authtoken')),
    path('', include(router.urls))
]
