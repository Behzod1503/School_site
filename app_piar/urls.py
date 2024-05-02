from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import (
    NewsModelViewSet,
    AnonsModelViewSet,
    VacancyModelViewSet,
    PhotoGalleryModelViewSet,
    VideoGalleryModelViewSet
)

router = DefaultRouter()

router.register(r'news', NewsModelViewSet, basename='news')
router.register(r'anons', AnonsModelViewSet, basename='anons')
router.register(r'vacancy', VacancyModelViewSet, basename='vacancy')
router.register(r'photos', PhotoGalleryModelViewSet, basename='photos')
router.register(r'videos', VideoGalleryModelViewSet, basename='videos')

urlpatterns = [

] + router.urls
