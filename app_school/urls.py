from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CEOModelViewSet

router = DefaultRouter()
router.register(r'ceo', CEOModelViewSet, basename='ceo')

urlpatterns = [
] + router.urls
