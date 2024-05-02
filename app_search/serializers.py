from rest_framework.serializers import Serializer

from app_pages.serializers import DocumentsSerializer

from app_piar.serializers import (
    NewsSerializer, AnonsSerializer,
    VacancySerializer, PhotoGallerySerializer,
    VideoGallerySerializer,
)


class UniversalSearchSerializer(Serializer):
    anons = AnonsSerializer(many=True)
    news = NewsSerializer(many=True)
    docs = DocumentsSerializer(many=True)
    vacancy = VacancySerializer(many=True)
    videos = VideoGallerySerializer(many=True)
    photos = PhotoGallerySerializer(many=True)

