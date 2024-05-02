from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import (
    SchoolInfoViewSet,
    DocumentsViewSet,
    DocumentsSearchAPIView
)


router = DefaultRouter()
router.register(r'infos', SchoolInfoViewSet)
router.register(r'docs', DocumentsViewSet)

urlpatterns = router.urls

urlpatterns += [
    path('search/docs/<str:title>/', DocumentsSearchAPIView.as_view()),
]