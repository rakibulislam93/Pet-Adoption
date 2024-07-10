from rest_framework.routers import DefaultRouter
from django.urls import path,include
from . import views

router = DefaultRouter()

router.register('list',views.PetViewSet)
router.register('category',views.CategoryViewSet)
router.register('adoption',views.AdoptionViewSet)
router.register('reviews',views.ReviewViewSet)


urlpatterns = [
    path('',include(router.urls)),
]
