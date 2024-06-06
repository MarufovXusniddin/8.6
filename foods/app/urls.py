from django.urls import path, include
from .views import FoodTypeViewSet, FoodViewSet, CommentViewSet
from rest_framework.routers import SimpleRouter, DefaultRouter

router = DefaultRouter()
router.register(r'foodtypes', FoodTypeViewSet, basename='foodtype')
router.register(r'foods', FoodViewSet, basename='food')
router.register(r'comments', CommentViewSet, basename='comment')

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
]